# LIDC-IDRI-Nodule Detection Code
Personal toolbox for lidc-idri dataset / lung cancer / nodule  
This project is a piece of shit, but it can really help to get information from LIDC-IDRI.  
I am willing to make it better with your help. 
Code in codeForLIDC is used for LIDC-IDRI researches. Code in codeforclinic is for our clinical researches.

## Key code in CodeForLIDC
#### *get_PatientId_SeriesUID.py*
It gives out the *id_scan.txt*, which can help to to load CT files according to patient Id.

#### *get_scan_xml.py*
It gets nodule's id and it's nine features from the xml files and gives out *nodule_chara_list.csv*.

#### *orignize_list_nodule_chara.py*
It gives out the *malignancy.csv*, which combine the *nodule_chara_list.csv* and the *list3.2.csv*. With *malignancy.csv*, you can get all information about labeled nodules.

#### *get_dicom_info.py*
It can get nodules' images and labels with *malignancy.csv* and *id_scan.txt*.

By running this code, you can have nodule images and their masks (single mask)
![nodule images and their masks (single mask)](https://github.com/qiuliwang/LIDC-IDRI-Toolbox-python/blob/master/codeForLIDC/samples.png)

#### *get_item.py*
It gets information from *dicom* files.  

#### *preparedicom.py*
It screens suitable CT series for deep learning from clinic raw data.

## CodeForMulitpleAnnotations
Get nodules with multiple segmentation annotations.
The method have been used in [Wang, Qiuli, et al. "Uncertainty-Aware Lung Nodule Segmentation with Multiple Annotations." arXiv preprint arXiv:2110.12372 (2021)](https://arxiv.org/abs/2110.12372).

By running *get_data* in CodeForMulitpleAnnotations, you can have nodule images and their multiple annotations' intersection, union, and difference.
![nodule images](https://github.com/qiuliwang/LIDC-IDRI-Toolbox-python/blob/master/CodeForMulitpleAnnotations/samples.png)