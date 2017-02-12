import sqlite3
import re

conn = sqlite3.connect('countemails.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts ')
cur.execute('CREATE TABLE Counts ( org TEXT, count INTEGER) ')


fhand = open('mbox.txt')
for line in fhand:
    if not line.startswith('From: '): continue
    emailraw = re.findall('@(\S+[a-z])',line)
    if len(emailraw)< 1 : continue
    emaildomain = emailraw[0]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (emaildomain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org,count) values (?,1)', (emaildomain, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 where org = ? ', (emaildomain,))
    conn.commit()

