import sqlite3
from Tkinter import *

# -------------------------
# INITIALIZE DATABASE STUFF
# -------------------------

#open connection to database
conn = sqlite3.connect('test.db')
curs = conn.cursor()

#if they haven't already been created, create the various tables.
curs.execute('''create table if not exists tasks (_id integer primary key, name text, desc text)''')

#create sort_options and populate, if this hasn't already been done.
curs.execute('''create table if not exists sort_options (_id integer primary key, name text)''')
curs.execute('select * from sort_options')
r = len(curs.fetchall())
if r == 0:
    t = [('Priority'),
         ('Due Date'),
         ('Date Created'),
         ('Completion')]

    for row in xrange(0, len(t)):
        curs.execute("insert into sort_options values (NULL, ?)", [t[row]])

#just for testing
curs.execute("select name from sort_options ORDER BY '_id'")
for row in curs:
    print row

#conn.commit()
#conn.close()


# ---------
# GUI STUFF
# ---------

class GUIFramework(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Type Some Text")
        self.config(bg='#e8e8e8')
        self.grid(padx=10, pady=0)
        self.pack(expand=YES, fill=BOTH)
        self.CreateWidgets()

    def CreateWidgets(self):
        self.lbText = Label(self, text="Sort Options")
        self.lbText.config(bg='#e8e8e8')
        self.lbText.grid(row=0, column=0)
        
        curs.execute("select name from sort_options ORDER BY '_id'")
        x = len(curs.fetchall())
        print x
        curs.execute("select name from sort_options ORDER BY '_id'")


        btn = range(x)
        r = 1
        for row in curs:
            btn[r-1] = Button(self, text=row)
            btn[r-1].config(bg='#afcefc', relief=FLAT)
            btn[r-1].grid(row=r, column=0)
            #btn[r-1].pack(expand=YES, fill=X)
            
            r = r + 1

        #btn[0].pack(expand=YES, fill=X)
            
if __name__ == "__main__":
    guiFrame = GUIFramework()
    guiFrame.mainloop()
