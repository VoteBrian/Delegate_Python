import sqlite3

# ----------
# INITIALIZE
# ----------

# Open Database Connection
conn = sqlite3.connect('test.db')
curs = conn.cursor()
    
# Create sort_options table and populate
curs.execute('''create table if not exists sort_options (_id integer primary key, name text)''')
curs.execute('select * from sort_options')
r = len(curs.fetchall())
if r == 0:
    t = [("Priority"),
         ("Due Date"),
         ("Date Created"),
         ("Completion")]

    for row in xrange(0, len(t)):
        curs.execute("insert into sort_options values (NULL, ?)", [t[row]])
    
    
# Create tasks table
curs.execute('''create table if not exists tasks (_id integer primary key,
                                                task_title text,
                                                task_desc text,
                                                assignee text)''')


# -----------------
# UTILITY FUNCTIONS
# -----------------
def getAllTasks():
    curs.execute('select * from tasks')
    return curs

def getNumTasks():
    curs.execute('select _id from tasks')
    return len(curs.fetchall())

def createTask(title, desc, asignee):
    curs.execute('insert into tasks values (NULL, ?, ?, ?)', [title, desc, asignee])
    conn.commit()

def getSortNames():
    curs.execute('select name from sort_options')
    return curs
