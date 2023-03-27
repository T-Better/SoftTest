# 读取test.xml中根节点标签名、二级节点标签、所有属性、name属性、内容
import xml.etree.ElementTree as et

path1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 04 Python_XML\test.xml'
tree = et.parse(path1)
root = tree.getroot()
print(root.tag)
# for child in root:
#     print(child.tag, child.text)
#     print(child.attrib.get('name'))
#     print(child.attrib.get('vendor'))

# 将hosts改为host2并另存为test_alter_今天日期.xml
for node in root.iter('host2'):
    node_tmp = 'host'
    print(node.tag)
    node.tag = node_tmp
    print(node.tag)

tree.write('test_alter_20220406.xml')
