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
root = Tk()
btn_side = range(4)

container_Frame = Frame(root)
container_Frame.config(bg="#e8e8e8", pady=10, padx=2)
container_Frame.pack(fill=BOTH, expand=1)

sidePanel = Frame(container_Frame)
sidePanel.config(bg="#e8e8e8")

curs.execute('select name from sort_options')
r=0
for row in curs:
    btn_side[r] = Button(sidePanel, text=row)
    btn_side[r].config(anchor=W, relief=FLAT, bg="#e8e8e8")
    btn_side[r].pack(side=TOP, fill=X)

    div = Frame(sidePanel)
    div.config(bg="#ffffff", height=1, relief=FLAT)
    div.pack(fill=X, pady=2, padx=2)

    r = r+1

sidePanel.pack(side=LEFT, fill=BOTH)


main_panel = Frame(container_Frame)
main_panel.config(bg="#ffffff")

new_task = Button(main_panel, text="+ Create Task")
new_task.config(bg="#d9d9d9", relief=FLAT)
new_task.pack(padx=2, pady=2, side=TOP, fill=X)

div = Frame(main_panel)
div.config(height=2, bd=1, relief=SUNKEN)
div.pack(fill=X, pady=2, padx=2)

new_task = Checkbutton(main_panel, text="Finish Delegate program")
new_task.config(bg="#ffffff", anchor=W, relief=FLAT)
new_task.pack(side=TOP, fill=X)

div = Frame(main_panel)
div.config(height=2, bd=1, relief=SUNKEN)
div.pack(fill=X, pady=2, padx=2)

new_task = Checkbutton(main_panel, text="Figure out why your spent time on this")
new_task.config(bg="#ffffff", anchor=W, relief=FLAT)
new_task.pack(side=TOP, fill=X)

div = Frame(main_panel)
div.config(height=2, bd=1, relief=SUNKEN)
div.pack(fill=X, pady=2, padx=2)

new_task = Checkbutton(main_panel, text="Laundry")
new_task.config(bg="#ffffff", anchor=W, relief=FLAT)
new_task.pack(side=TOP, fill=X)

div = Frame(main_panel)
div.config(height=2, bd=1, relief=SUNKEN)
div.pack(fill=X, pady=2, padx=2)

new_task = Checkbutton(main_panel, text="Drink at least 6 beers")
new_task.config(bg="#ffffff", anchor=W, relief=FLAT)
new_task.pack(side=TOP, fill=X)

div = Frame(main_panel)
div.config(height=2, bd=1, relief=SUNKEN)
div.pack(fill=X, pady=2, padx=2)

new_task = Checkbutton(main_panel, text="Nurse hangover")
new_task.config(bg="#ffffff", anchor=W, relief=FLAT)
new_task.pack(side=TOP, fill=X)

div = Frame(main_panel)
div.config(height=2, bd=1, relief=SUNKEN)
div.pack(fill=X, pady=2, padx=2)

main_panel.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()
