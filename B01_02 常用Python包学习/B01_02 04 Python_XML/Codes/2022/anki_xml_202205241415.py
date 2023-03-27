import xml.etree.ElementTree as et

tree = et.parse('../../test.xml')
root = tree.getroot()
print(root.tag)
for child in root:
    print(child.tag, child.text)
    print(child.attrib.get('name'))
    print(child.attrib.get('vendor'))

# 将hosts改为host2并另存为test_alter_今天日期.xml
for node in root.findall('hosts'):
    print(node.tag)
    node.tag = 'host2'
    print(node.tag)
tree.write('test_alter_20220524.xml')

