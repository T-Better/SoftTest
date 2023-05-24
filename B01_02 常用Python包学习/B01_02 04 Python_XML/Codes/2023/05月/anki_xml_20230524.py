import xml.etree.ElementTree as et


tree = et.parse()
root = tree.getroot()

for n in root.findall('hosts'):
    print(n.tag)
    n.tag = 'host2'

tree.write('')












