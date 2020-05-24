# LIDC-IDRI-Toolbox-python
Personal toolbox for lidc-idri dataset / lung cancer / nodule  
This code is a piece of shit, but it can really help to get information from LIDC-IDRI.  
I am willing to make it better with your help.

### Key code in codeForLIDC
#### get_PatientId_SeriesUID.py 
It gives out the *id_scan.txt*, which can help to to load CT files according to patient Id.

#### get_scan_xml.py
It get nodule's id and it's nine features from the xml files and gives out *nodule_chara_list.csv*.

#### orignize_list_nodule_chara.py
It gives out the *malignancy.csv*, which combine the *nodule_chara_list.csv* and the *list3.2.csv*. With *malignancy.csv*, you can get all information about labeled nodules.

#### get_dicom_info.py
It can get nodules' images and labels with *malignancy.csv* and *id_scan.txt*.