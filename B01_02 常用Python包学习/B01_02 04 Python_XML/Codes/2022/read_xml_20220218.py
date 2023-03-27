import xml.etree.ElementTree as ET
tree = ET.parse('../../test.xml')  # 打开
root = tree.getroot()  # 建立根节点
print(root.tag)  # 根节点元素的tag属性
for child in root:
    print("=======================")
    print(child.tag, child.text)  # 耳机节点标签、属性、内容
    print("————————")
    print(child.attrib.get('name'))
    print(child.attrib.get('vendor'))