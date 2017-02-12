import xml.etree.ElementTree as ET
tree = ET.parse('xmlsample.xml')
#root = ET.fromstring('xmlsample.xml')
root = tree.getroot()
for child in root:
    print child.tag, child.attrib


for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print name, rank