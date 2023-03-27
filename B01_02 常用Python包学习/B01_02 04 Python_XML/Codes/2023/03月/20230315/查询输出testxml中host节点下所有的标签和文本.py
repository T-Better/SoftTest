import xml.etree.ElementTree as et


# 获取xml，建立树结构
tree = et.parse('../../../../test.xml')

# 定义根节点
root = tree.getroot()

# 找到所有host节点，然后遍历其子节点和子子节点等，打印标签名和内容
for n in root.iter('host'):
    for n1 in n:
        print(n1.tag,n1.text)
        print('--------------------------')






