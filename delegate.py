import sqlite3
from Tkinter import *

#open connection to database
conn = sqlite3.connect('test.db')
curs = conn.cursor()

#if they haven't already been created, create the various tables.
curs.execute('''create table if not exists tasks (_id integer primary key, name text, desc text)''')
curs.execute('''create table if not exists sort_options (_id integer primary key, name text)''')
curs.execute('select * from sort_options')
if curs < 1:
    t = [('Priority'),
         ('Due Date'),
         ('Date Created'),
         ('Completion')]

    for r in xrange(0, len(t)):
        curs.execute("insert into sort_options values (NULL, ?)", [t[r]])

#just for testing
curs.execute('select * from sort_options')
for row in curs:
    print row

conn.commit()
conn.close()
