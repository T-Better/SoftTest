import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')
root = tree.getroot()
for node in root.findall('hosts'):
    print(node.tag,node.text)
    node.tag = "hosts2"
    print(node.tag,node.text)
tree.write('test_...')















