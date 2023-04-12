import xml.etree.ElementTree as et



xmlf=r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 04 Python_XML\test.xml'

tree = et.parse(xmlf)
root = tree.getroot()
for n in tree.iters('hosts'):
    print(n.tag)
    n.tag = 'host2'

tree.write('test_alter_20230412.xml')
