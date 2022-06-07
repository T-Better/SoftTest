import xml.etree.ElementTree as et

tree = et.parse('test.xml')
root = tree.getroot()
for node in root.iter('host'):
    for i in node:
        print(i.tag)
        print(i.text)


