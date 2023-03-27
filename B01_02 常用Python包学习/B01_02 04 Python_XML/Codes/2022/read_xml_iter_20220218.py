import xml.etree.ElementTree as ET

tree = ET.parse("../../test.xml")
root = tree.getroot()
for node in root.iter('host'):
    for i in node:
        print(i.tag, i.text)
        print("-----------------")

