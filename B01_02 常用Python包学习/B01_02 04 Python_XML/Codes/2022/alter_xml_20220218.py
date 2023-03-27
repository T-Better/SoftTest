import xml.etree.ElementTree as ET

tree = ET.parse('../../test.xml')
root = tree.getroot()
for node in root.findall('hosts'):  # 查找二级节点所有hosts的子节点
    print(node.tag, node.text)
    temp_node = 'hosts2'
    node.tag = temp_node  # 将二级节点hosts下的三级节点都改成host2
    print(node.tag, node.text)
tree.write('test_alter_result.xml')  # 保存
