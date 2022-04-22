import xml.etree.ElementTree as et


tree = et.parse('test.xml')
root = tree.getroot

for node in root.findall('hosts'):
    node.tag = 'host2'
    print(node.tag)

tree.write('test.xml')











