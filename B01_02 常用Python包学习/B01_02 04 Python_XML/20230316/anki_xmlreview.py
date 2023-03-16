# xml复习
import xml.etree.ElementTree as et


# 读取xml，建立树结构
tree = et.parse('../test.xml')

# 定义根节点
root = tree.getroot()

# iter和findall区别
for n in root.iter():
    print(n.tag, n.attrib.get('name'),n.attrib.get('vendor'), n.text)
    print('-------------------------')
    # n.tag = 'host2'
    # print(n.tag, n.attrib.get('name'))
    # print('============================')

# tree.write('./test_alter_20230316')

