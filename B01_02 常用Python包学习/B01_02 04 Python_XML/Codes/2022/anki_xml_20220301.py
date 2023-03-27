import xml.etree.ElementTree as et

path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_06 工具学习\009 Python_XML\test.xml'
tree = et.parse(path1)
root = tree.getroot()
print(root.tag)
for nodes in root:
    print(nodes.tag,nodes.attrib,nodes.text)
    for node in nodes:
        print(node.tag, node.text)
        print(node.attrib.get('name'))
