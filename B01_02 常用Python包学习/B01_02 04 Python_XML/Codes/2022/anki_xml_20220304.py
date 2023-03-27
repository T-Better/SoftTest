import xml.etree.ElementTree as ET


path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_06 工具学习\009 Python_XML\test.xml'

tree = ET.parse(path1)
root = tree.getroot()

for node in root.iter('host'):
    for child in node:
        print(child.tag, child.text)

