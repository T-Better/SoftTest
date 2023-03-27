import xml.etree.ElementTree as ET

tree = ET.parse('../../test.xml')
root = tree.getroot()
"""
for node in root.iter('host'):
    for n in node:
        print(n.tag, n.text)
"""

# 将hosts改为host2并另存为test_alter_今天日期.xml
for node in root.iter('hosts'):
    print(node.tag)
    tmp_tag = 'host2'
    node.tag = tmp_tag
tree.write('test_alter_20220223.xml')






