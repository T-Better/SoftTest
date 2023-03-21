import xml.etree.ElementTree as et


# 请求数据，建立树结构
tree = et.parse('../test.xml')

# 建立根节点
root = tree.getroot()

for n in root.iter():
    print(n.tag,n.attrib.get('name'),n.attrib.get('vendor'),n.text)
    print('-----------------')
    # n.tag = 'host2'
    # print(n.tag)

# tree.write('./test_alter_20230320.xml')




