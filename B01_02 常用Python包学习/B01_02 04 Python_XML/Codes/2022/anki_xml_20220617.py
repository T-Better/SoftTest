import xml.etree.ElementTree as et

tree = et.parse('../../test.xml')
root = tree.getroot()
print(root.tag)
for node in root:
    print(node.tag)
    print(node.attrib.get('vendor'))

