import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 465 1023
    </phone>
    <email hide="yes"/>
    <name>Don</name>
    <phone type="intl">
        +1 734 465 1023
    </phone>
    <email hide="yes"/>
    <name>PetSmart</name>
    <phone type="intl">
        +1 734 465 1023
    </phone>
    <email hide="yes"/>
</person>
'''

xmlsample = ET.fromstring(data)
lst = xmlsample.findall('name')
print 'User Count: ', len(lst)

for item in lst:
    print 'Name: ' , item.find('name').text


#print 'Name: ' , xmlsample.findall('name')
#print 'Phone: ' , xmlsample.findall('phone').text.strip()
#print 'Attr: ' , xmlsample.findall('email').get('hide')

print xmlsample.text
