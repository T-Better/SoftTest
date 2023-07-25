import xml.etree.ElementTree as et

p=r''
tree = et.parse(p)

root = tree.getroot()

for n in root.findall('hosts'):
    print(n.tag)
    n.tag = 'host2'

tree.write()























