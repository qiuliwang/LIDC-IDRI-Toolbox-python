### Func_get_PatientId_SeriesUID, get_PatientId_SeriesUID, orignize_list_nodule_chara are key codes  
they generate files like malignancy.csv, PatientId_SeriesUID.csv which can make LIDC easier to use

### Key code in codeForLIDC
#### get_PatientId_SeriesUID.py 
It gives out the *id_scan.txt*, which can help to to load CT files according to patient Id.

#### get_scan_xml.py
It get nodule's id and it's nine features from the xml files and gives out *nodule_chara_list.csv*.

#### orignize_list_nodule_chara.py
It gives out the *malignancy.csv*, which combine the *nodule_chara_list.csv* and the *list3.2.csv*.