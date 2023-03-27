import xml.etree.ElementTree as et

tree = et.parse('../../test.xml')
root = tree.getroot()

for node in root.iter('host'):
    print(node.tag)
    print(node.text)
    print(node.attrib.get('name'))














