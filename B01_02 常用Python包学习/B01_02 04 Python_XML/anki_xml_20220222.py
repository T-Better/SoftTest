"""
将hosts改为host2并另存为test_alter_今天日期.xml
"""
import xml.etree.ElementTree as et

path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_06 工具学习\009 Python_XML\test.xml'
tree = et.parse(path1)
root = tree.getroot()
for node in root.findall('hosts'):
    print(node.tag, node.text)  # 改之前检查
    node_tmp = 'host2'
    node.tag = node_tmp  # 进行修改
    print(node.tag, node.text)  # 修改后再检查

tree.write('test_alter_20220222.xml')
