import xml.etree.ElementTree as et


path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_06 工具学习\009 Python_XML\test.xml'
tree = et.parse(path1)
root = tree.getroot()
print(root.tag)
for child in root.iter():
    print(child.tag)
    print("---------------")
    print(child.attrib.get('name'))
    print(child.attrib.get('vendor'))




