#-*- coding: UTF-8 -*-

import pydicom
import cv2
import os
import shutil
import tqdm
import numpy as np 
import matplotlib.pyplot as plt
from skimage import measure, morphology
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import scipy.ndimage

pathdir = './test/'
npypathdir = '/raid/data/clinic/data/cutpathologynpy/'

patients = os.listdir('./test/')
print(len(patients))

def get_pixels_hu(slices):
    image = np.stack([s.pixel_array for s in slices])
    # Convert to int16 (from sometimes int16),
    # should be possible as values should always be low enough (<32k)
    image = image.astype(np.int16)
    # Set outside-of-scan pixels to 0
    # The intercept is usually -1024, so air is approximately 0
    image[image == -2000] = 0
    # Convert to Hounsfield units (HU)
    for slice_number in range(len(slices)):
        intercept = slices[slice_number].RescaleIntercept
        slope = slices[slice_number].RescaleSlope
        if slope != 1:
            image[slice_number] = slope * image[slice_number].astype(np.float64)
            image[slice_number] = image[slice_number].astype(np.int16)
        image[slice_number] += np.int16(intercept)
    return np.array(image, dtype=np.int16)

def resample(image, scan, new_spacing=[1,1,1]):
    # Determine current pixel spacing
    slicethickness = (scan[0].SliceThickness)
    pixel_spacing = list(scan[0].data_element("PixelSpacing"))
    spacing = map(float, ([slicethickness] + pixel_spacing))

    spacing = np.array(list(spacing))
    # print("here here:　",spacing)
    resize_factor = spacing / new_spacing
    new_real_shape = image.shape * resize_factor
    new_shape = np.round(new_real_shape)
    real_resize_factor = new_shape / image.shape
    new_spacing = spacing / real_resize_factor
 
    image = scipy.ndimage.interpolation.zoom(image, real_resize_factor, mode='nearest')
 
    return image, new_spacing

def plot_3d(image, threshold=70):
    # Position the scan upright,
    # so the head of the patient would be at the top facing the camera

    p = image#.transpose(2,1,0)

    # p = image
    verts, faces = measure.marching_cubes_classic(p, 70)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    # Fancy indexing: `verts[faces]` to generate a collection of triangles
    mesh = Poly3DCollection(verts[faces], alpha=0.1)
    face_color = [0.5, 0.5, 1]
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)
    ax.set_xlim(0, p.shape[0])
    ax.set_ylim(0, p.shape[1])
    ax.set_zlim(0, p.shape[2])
    plt.savefig("examples3.jpg")
    # plt.show()

def largest_label_volume(im, bg = -1):
    vals, counts = np.unique(im, return_counts = True)

    counts = counts[vals != bg]
    vals = vals[vals != bg]

    if len(counts) > 0:
        return vals[np.argmax(counts)]
    else:
        return None
    
def normalize(image):
    image = (image - MIN_BOUND) / (MAX_BOUND - MIN_BOUND)
    image[image>1] = 1.
    image[image<0] = 0.
    return image

def cutTheImage(slices):
    res = []
    for slice in slices:
        res.append(slice[60:400, 0:512])
    return np.array(res)

for patient in tqdm.tqdm(patients):
    dcmfiles = os.listdir(os.path.join(pathdir, patient))
    slices = [pydicom.dcmread(os.path.join(pathdir, patient, s)) for s in dcmfiles]
    slices.sort(key = lambda x : float(x.ImagePositionPatient[2]),reverse=True)
    patient_pixels = get_pixels_hu(slices)#.transpose(2,1,0)
    plot_3d(patient_pixels)
    # patient_pixels = cutTheImage(patient_pixels)
    # pix_resampled, new_spacing = resample(patient_pixels, slices, [1, 1, 1])

    # np.save(npypathdir + patient, pix_resampled)
# 