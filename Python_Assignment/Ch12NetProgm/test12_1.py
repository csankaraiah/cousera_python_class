import re

urlin = 'http://www.py4inf.com/code/romeo.txt'
website = re.findall('www\S+com',urlin)
print website
