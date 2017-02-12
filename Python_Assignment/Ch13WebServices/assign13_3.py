import urllib
import json

location = raw_input("Enter Location: ")

locurl = 'http://python-data.dr-chuck.net/geojson?'

urlin = locurl + urllib.urlencode({'sensor':'false', 'address': location})

print 'Retreving ' + urlin

data = urllib.urlopen(urlin).read()
data1 = json.loads(data)

#data2= json.dumps(data1)
#print 'Retrieved ', len(data2)
place_id_out = data1["results"][0]["place_id"]
print 'Place id ', place_id_out