import xml.etree.ElementTree as et

tree = et.parse('../../test.xml')
root = tree.getroot()
for node in root.iter('hosts'):
    print(node.tag)
    temp_tag = 'host2'
    node.tag = temp_tag

tree.write('./test_20220322.xml')
