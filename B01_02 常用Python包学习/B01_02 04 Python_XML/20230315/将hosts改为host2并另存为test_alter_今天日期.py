import xml.etree.ElementTree as et


# 读取数据，建立树结构
tree = et.parse('../test.xml')

# 定义根节点
root = tree.getroot()

# 获取hosts节点，改名
for n1 in root.findall('hosts'):
    print(n1.tag)
    n1.tag = 'host3'
    print(n1.tag)

# 保存
tree.write('./test_alter_202303150935.xml')