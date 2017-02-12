import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('itune.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


fname = 'Library.xml'
etree = ET.parse(fname)
all = etree.findall('dict/dict/dict')

for row in all:
    track_name = lookup(row, 'Name')
    artist_name = lookup(row, 'Artist')
    genre_name = lookup(row, 'Genre')
    album_title = lookup(row, 'Album')
    track_len = lookup(row, 'Total Time')
    track_rating = lookup(row, 'Rating')
    track_count = lookup(row, 'Play Count')

    if artist_name is None or genre_name is None or album_title is None: continue

    print track_name, artist_name, genre_name, album_title

    cur.execute(''' INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist_name,))
    cur.execute('SELECT id from artist where name = ?', (artist_name,))
    artist_id = cur.fetchone()[0]

    cur.execute(''' INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre_name,))
    cur.execute('SELECT id from Genre where name = ?', (genre_name,))
    genre_id = cur.fetchone()[0]

    cur.execute(''' INSERT OR IGNORE INTO Album (artist_id,title) VALUES (?,?)''', (artist_id, album_title))
    cur.execute('SELECT id from Album where artist_id = ? and title = ?', (artist_id, album_title))
    try:
        album_id = cur.fetchone()[0]
    except:
        print ' here is the bad data ', track_name,'|', artist_name,'|', artist_id,'|', album_title
        print track_name, artist_name, artist_id, genre_name, album_title
    cur.execute(''' INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,?)''',
                (track_name, album_id, genre_id,track_len, track_rating, track_count))

    conn.commit()
