import xml.etree.ElementTree as et

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 04 Python_XML\test.xml'
tree = et.parse(p1)  # 建立树结构
root = tree.getroot()  # 确定根节点
for n in root.iter('hosts'):
    print(n.tag, n.attrib.get('name'), n.attrib.get('vendor'), n.text)
    n.tag = 'host2'

tree.write('test_alter_20230327.xml')
