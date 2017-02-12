import json
import urllib

urlin = raw_input("Enter Location: ")
#urlin = 'http://python-data.dr-chuck.net/comments_42.json'
print 'Retrieving' , urlin
data = urllib.urlopen(urlin).read()

info = json.loads(data)
count = 0
sum = 0

for item in info["comments"]:
    sum = sum + int(item["count"])
    count = count + 1
print 'Count: ', count
print 'Sum: ', sum