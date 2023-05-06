import xml.etree.ElementTree as et



tree = et.parse()
root = tree.getroot()

for n in root.find('hosts'):
    print(n.tag)
    n.tag = 'host2'
    print(n.tag)

tree.write()








