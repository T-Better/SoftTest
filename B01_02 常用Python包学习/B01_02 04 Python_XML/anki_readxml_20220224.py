import xml.etree.ElementTree as ET

path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_06 工具学习\009 Python_XML\test.xml'
tree = ET.parse(path1)
root = tree.getroot()
print(root.tag)
for node in root:
    print(node.tag, node.text)
    print('——————————————')
    print(node.attrib.get('name'))
