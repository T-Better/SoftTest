import xml.etree.ElementTree as et

path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_06 工具学习\009 Python_XML\test.xml'
tree = et.parse(path1)
root = tree.getroot()

for children in root.iter('host'):
    print(children.tag, children.text,children.attrib)
    for child in children:
        print(child.tag, child.text, child.attrib)

