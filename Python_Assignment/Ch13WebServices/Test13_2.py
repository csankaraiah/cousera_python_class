import xml.etree.ElementTree as ET

# noinspection PyByteLiteral
data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Ben</name>
        </user>
    </users>
</stuff>
'''

xmlsample = ET.fromstring(data)
lst = xmlsample.findall('users/user')
print 'User Count: ', len(lst)
print lst

for item in lst:
    print 'Name: ' , item.find('name').text
    print 'Id: ' , item.find('id').text
    print 'Attribute: ' , item.get('x')
    print ''

#print 'Name: ' , xmlsample.findall('name')
#print 'Phone: ' , xmlsample.findall('phone').text.strip()
#print 'Attr: ' , xmlsample.findall('email').get('hide')

print xmlsample.text
