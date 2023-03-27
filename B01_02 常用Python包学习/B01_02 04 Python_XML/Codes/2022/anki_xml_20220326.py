import xml.etree.ElementTree as et

p1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_06 工具学习\009 Python_XML\test.xml'
tree = et.parse(p1)
root = tree.getroot()
print(root.tag)
for node in root.iter('host'):
    for child in node:
        print(child.tag)





