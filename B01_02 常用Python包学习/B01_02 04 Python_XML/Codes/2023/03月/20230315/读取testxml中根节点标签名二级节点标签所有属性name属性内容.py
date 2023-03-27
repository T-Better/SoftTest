"""
读取D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 04 Python_XML\test.xml
中根节点标签名、二级节点标签、所有属性、name属性、内容
"""
import xml.etree.ElementTree as et


# 读取xml，建立树结构
tree = et.parse('../../../../test.xml')

# 定义根节点
root = tree.getroot()
print(root.tag)

# 读取root下面子节点的tag、name、vendor、值
for n in root.findall('host'):
    print(n.tag, n.text)
    print('-----------')
    # print(n.tag, n.attrib.get('name'), n.attrib.get('vendor'),n.text)



