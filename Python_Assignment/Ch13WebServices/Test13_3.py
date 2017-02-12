import json

data = '''
[
 { "id" : "001",
   "x" : "2",
   "name" : "Chuck"
 },
 { "id" : "009",
   "x" : "7",
   "name" : "Ben"
 }
]'''

info = json.loads(data)
print 'User Count: ', len(info)

for item in info:
    print 'Name:',item['name']
#print 'Hide:',info["id"]