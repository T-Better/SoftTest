import xml.etree.ElementTree as et


p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 04 Python_XML\test.xml'

tree = et.parse(p)
root = tree.getroot()

for n in root.iter():
    for e in n:
        print(e.tag, e.attrib['name'],e.attrib['vendor'],e.text)


