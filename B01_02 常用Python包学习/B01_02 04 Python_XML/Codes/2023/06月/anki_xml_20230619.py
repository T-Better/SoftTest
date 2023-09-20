import xml.etree.ElementTree as et


p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 04 Python_XML\test.xml'
tree = et.parse(p1)
root = tree.getroot()

for n in root.findall('hosts'):
    print(n.tag)
    n.tag = 'host2'
    print(n.tag)

tree.write(p1)





