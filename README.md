# LIDC-IDRI-Nodule Analysis Code
Personal toolbox for lidc-idri dataset / lung cancer / nodule  
This project is a piece of shit, but it can really help to get information from LIDC-IDRI.  
I am willing to make it better with your help. 

Code in codeForLIDC is used for LIDC-IDRI researches. 
For the label information, you can refer to [Shen S , Han S X , Aberle D R , et al. An Interpretable Deep Hierarchical Semantic Convolutional Neural Network for Lung Nodule Malignancy Classification[J]. 2018.](<https://arxiv.org/abs/1806.00712>).

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
The method has been used in [Wang, Qiuli, et al. "Uncertainty-Aware Lung Nodule Segmentation with Multiple Annotations." arXiv preprint arXiv:2110.12372 (2021)](https://arxiv.org/abs/2110.12372). You can get the processed data here: https://pan.baidu.com/s/1nQLaS_NEaiBeGOeHxHV1dg, Code: 4f38

#### *xmlopt.py*
It can extract label edges from xml files.

#### *get_data.py*
By running *python get_data.py* in CodeForMulitpleAnnotations, you can have nodule images and their multiple annotations' intersection, union, and difference.

![nodule images](https://github.com/qiuliwang/LIDC-IDRI-Toolbox-python/blob/master/CodeForMulitpleAnnotations/samples.png)

If you find it helpful to your research, please cite as follows:
```
@inproceedings
{yang2022uncertainty,
 title={Uncertainty-Guided Lung Nodule Segmentation with Feature-Aware Attention},
 author={Yang, Han and Shen, Lu and Zhang, Mengke and Wang, Qiuli},
 booktitle={Medical Image Computing and Computer Assisted Intervention--MICCAI 2022: 25th International Conference, Singapore, September 18--22, 2022,    Proceedings, Part V},
 pages={44--54},
 year={2022},
 organization={Springer}
}

@inproceedings{wang2020class,
  title={Class-aware multi-window adversarial lung nodule synthesis conditioned on semantic features},
  author={Wang, Qiuli and Zhang, Xingpeng and Chen, Wei and Wang, Kun and Zhang, Xiaohong},
  booktitle={Medical Image Computing and Computer Assisted Intervention--MICCAI 2020: 23rd International Conference, Lima, Peru, October 4--8, 2020, Proceedings, Part VI 23},
  pages={589--598},
  year={2020},
  organization={Springer}
}
```

Feel free to contact me (qiuli.wang0102@foxmail.com) if you have any problems.
