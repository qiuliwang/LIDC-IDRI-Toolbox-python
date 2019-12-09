'''
Created by WangQL

6/27/2018

operation for xml files
get structure of xml files from LIDC
'''

try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 
import sys,os

tree = ET.parse('069.xml') 
root = tree.getroot() 

for child in root:
    # print('child')
    print(child.tag)
    for leaves in child:
        # print('    lefe')
        print('    ',leaves.tag)
        for dot in leaves:
            # print('        dot')
            print('        ',dot.tag)
            for last in dot:
                if not last.tag.find('edgeMap'):
                    # print('            last')
                    print('            ', last.tag)
                # for test in last:
                #     print('                test')
                #     print('                ', test.tag, test.attrib)
