import xml.etree.ElementTree as et

path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_06 工具学习\009 Python_XML\tet.xml'
tree = et.parse(path1)
root = tree.getroot()
print(root.tag)
tmp_tag = 'host2'
for node in root:
    print(node.tag, node.text)
    for child in node:
        child.tag = tmp_tag
        print(child.tag, child.text)
        print(child.attrib.get('name'))
        print(child.attrib.get('vendor'))
tree.write()



