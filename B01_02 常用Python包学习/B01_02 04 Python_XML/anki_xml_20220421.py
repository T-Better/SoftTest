import xml.etree.ElementTree as ET
xp1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 04 Python_XML\test.xml'

tree = ET.parse('test.xml')
root = tree.getroot()
print(root.tag)
for child in root:
    print(child.tag, child.text)
    print(child.attrib.get('name'))
    print(child.attrib.get('vendor'))

