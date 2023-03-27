import xml.etree.ElementTree as et
xp1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 04 Python_XML\test.xml'

"""
tree = et.parse(xp1)
root = tree.getroot()
print(root.tag)
for n2 in root:
    print(n2.tag,n2.text)
    print(n2.attrib.get('name'))
    print(n2.attrib.get('vendor'))
"""

"""
tree = et.parse(xp1)
root = tree.getroot()
for n1 in root.iter('host'):
    for n2 in n1:
        print(n2.tag)
        print(n2.text)
        print('______________')
"""

tree = et.parse(xp1)
root = tree.getroot()
for n1 in root.findall('hosts'):
    n1.tag = 'host2'
    print(n1.tag)

tree.write(r'test_alter_20221010.xml')

