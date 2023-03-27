from xml.etree import ElementTree as ET

root = ET.Element('root', {'age':'50'})  # 创建根节点 设置属性age=18
son = ET.SubElement(root, 'son', {'age':'30'})
ET.SubElement(son, 'sunzi', {'age': '18'})
tree = ET.ElementTree(root)
tree.write('create_20220218.xml')


