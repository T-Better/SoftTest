import xml.etree.ElementTree as et
p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 04 Python_XML\test.xml'

tree = et.parse(p1)
root = tree.getroot()

for n in root.iter():
    print(n.tag,n.attrib.get('name'),n.attrib.get('vendor'))













