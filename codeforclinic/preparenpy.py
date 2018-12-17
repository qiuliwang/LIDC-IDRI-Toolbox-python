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

pathdir = '/raid/data/clinic/data/pathology2/'

patients = os.listdir(pathdir)
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
    # print(scan[0].SliceThickness)
    # spacing = map(float, ([scan[0].SliceThickness,scan[0].PixelSpacing]))
    # spacing = np.array(list(spacing))
    # resize_factor = spacing / new_spacing
    # new_real_shape = image.shape * resize_factor
    # new_shape = np.round(new_real_shape)
    # real_resize_factor = new_shape / image.shape
    # new_spacing = spacing / real_resize_factor
    image = scipy.ndimage.interpolation.zoom(image, 0.5, mode='nearest')
    return image

def plot_3d(image, threshold=-300):
    # Position the scan upright,
    # so the head of the patient would be at the top facing the camera
    p = image.transpose(0,1,2) #2
    p = p.transpose(2,1,0) #2
    p = p.transpose(2,1,0) #2

    # #p = image.transpose(0,2,1)3
    # p = image.transpose(0,2,1)#4

    # p = image
    verts, faces = measure.marching_cubes_classic(p, threshold)
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
    plt.savefig("examples1.jpg")
    plt.show()

for patient in patients[:1]:
    dcmfiles = os.listdir(os.path.join(pathdir, patient))
    # print(dcmfiles)
    slices = [pydicom.dcmread(os.path.join(pathdir, patient, s)) for s in dcmfiles]
    slices.sort(key = lambda x : float(x.ImagePositionPatient[2]),reverse=True)
    first_patient_pixels = get_pixels_hu(slices)
    print(type(first_patient_pixels))
    print(first_patient_pixels.shape)
    pix_resampled = resample(first_patient_pixels, slices, [1, 1, 1])
    print(pix_resampled.shape)
    plot_3d(pix_resampled, 400)
