import re

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 stephen.marquard@uct.ac.za '
y = re.findall('\S+@\S+', x)
print y