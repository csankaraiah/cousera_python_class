import socket
import re

urlin = raw_input('Enter the URL for the page : ')
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
website_raw = re.findall('www\S+com',urlin)
# website link GET http://www.py4inf.com/code/romeo.txt HTTP/1.0 \n\n
if len(website_raw) < 1: print 'not a valid URL'
website = website_raw[0]

try :
    mysocket.connect( (website, 80))
    mysocket.send('GET ' + urlin + 'HTTP/1.0 \n\n')
except:
    print 'Not a valid URL'

while True:
    data = mysocket.recv(512)
    if ( len(data) < 1): break

    print data

mysocket.close()