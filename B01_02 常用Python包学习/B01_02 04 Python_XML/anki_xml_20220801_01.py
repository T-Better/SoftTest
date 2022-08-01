import xml.etree.ElementTree as et

tree = et.parse('./test.xml')
root = tree.getroot()
print(root.tag)

for child in root.findall('hosts'):
    print(child.tag,child.text)
    child.tag = 'hosts2'
tree.write('test_alter_result.xml')







