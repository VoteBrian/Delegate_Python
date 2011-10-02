import sqlite3
from Tkinter import *

# --------------------
# FUNCTION DEFINITIONS
# --------------------
# utility functions
def getAllTasks():
    curs.execute('select * from tasks')
    return curs

def getNumTasks():
    curs.execute('select _id from tasks')
    return len(curs.fetchall())

def createTask():
    s = StringVar()
    s = new_task_entry.get()
    if len(s) > 0:
        curs.execute('insert into tasks values (NULL, ?, NULL, NULL)', [s])
        new_task_entry.delete(0, END)

        #delete all tasks for redraw
        deleteAllTaskRows()

        drawAllTasks()

    conn.commit()

def deleteAllTaskRows():
    numTasks = len(root.taskRow)
    for r in xrange(0, numTasks-1):
        root.taskRow[r].delete()    
    
def drawAllTasks():
    numTasks = getNumTasks()
    root.taskRow = range(numTasks)
    curs = getAllTasks()
    r = 0
    for row in curs:
        root.taskRow[r] = TaskRow()
        root.taskRow[r].setID(row[0])
        root.taskRow[r].setTitle(row[1])
        root.taskRow[r].draw()
        r = r+1

def testing():
    print "testing"

# -------
# CLASSES
# -------
class TaskRow:
    _title = "Default"
    _id = 0
    _desc = "Default"
    
    def setID(self, id):
        self._id = id
        
    def setTitle(self, title):
        self._title = title

    def setDesc(self, desc):
        self._desc = desc

    def setAssignee(self, assignee):
        self._assignee = assignee

    def draw(self):
        self.titleBtn = Checkbutton(main_panel, text=self._title)
        self.titleBtn.config(bg="#ffffff", anchor=W, relief=FLAT)
        self.titleBtn.pack(side=TOP, fill=X)
        
        self.div = Frame(main_panel)
        self.div.config(height=2, bd=1, relief=SUNKEN)
        self.div.pack(fill=X, pady=2, padx=2)

    def delete(self):
        self.titleBtn.destroy()
        self.div.destroy()

    

# -------------------------
# INITIALIZE DATABASE STUFF
# -------------------------

#open connection to database
conn = sqlite3.connect('test.db')
curs = conn.cursor()

#create sort_options and populate, if this hasn't already been done.
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

#create tasks and populate, if this hasn't already been done
curs.execute('''create table if not exists tasks (_id integer primary key,
                                                task_title text,
                                                task_desc text,
                                                assignee text)''')
curs.execute('select * from tasks')
r = len(curs.fetchall())
if r == 0:
    curs.execute('insert into tasks values (NULL, ?, ?, ?)', ["Update Egypt Drawings",
                 "Redraw to match standard release style", "Brian Flores"])

##curs.execute('select * from tasks')
##for row in curs:
##    print row

#conn.commit()
#conn.close()


# ---------
# GUI STUFF
# ---------
root = Tk()
root.title("Delegate")
root.geometry("800x600")
btn_side = range(4)

container_Frame = Frame(root)
container_Frame.config(bg="#e8e8e8", pady=10, padx=2, width=900)
container_Frame.pack(fill=BOTH, expand=1)

# -----------------
# CREATE SIDE PANEL
# -----------------
sidePanel = Frame(container_Frame)
sidePanel.config(bg="#e8e8e8")

# Options pulled from sort_options
sort_label = Label(sidePanel, text="Sort By:", font=("Arial", 8))
sort_label.config(bg="#e8e8e8")
sort_label.pack(side=TOP, fill=X)

div = Frame(sidePanel)
div.config(bg="#ffffff", height=1, relief=FLAT)
div.pack(fill=X, pady=2, padx=2)

curs.execute('select name from sort_options')
r=0
for row in curs:
    btn_side[r] = Button(sidePanel, text=row[0])
    btn_side[r].config(anchor=W, relief=FLAT, bg="#e8e8e8")
    btn_side[r].pack(side=TOP, fill=X)

    div = Frame(sidePanel)
    div.config(bg="#ffffff", height=1, relief=FLAT)
    div.pack(fill=X, pady=2, padx=2)

    r = r+1

# TODO
# Filter options

sidePanel.pack(side=LEFT, fill=BOTH)

# -----------------
# CREATE MAIN PANEL
# -----------------

# border
border_panel = Frame(container_Frame)
border_panel.config(bg="#cbcbcb", padx=1, pady=1)

# content
main_panel = Frame(border_panel)
main_panel.config(bg="#ffffff")

# add new task
task_str = StringVar()

new_task_container = Frame(main_panel)
new_task_container.config(bg="#ffffff")
new_task_container.pack(side=TOP, fill=X)

new_task_entry = Entry(new_task_container)
new_task_entry.config(bg="#d9d9d9")
new_task_entry.pack(side=LEFT, fill=BOTH, expand=1)

new_task_button = Button(new_task_container, command=createTask)
new_task_button.config(text="Create Task")
new_task_button.pack(side=LEFT, fill=X, expand=0)

div = Frame(main_panel)
div.config(height=2, bd=1, relief=SUNKEN)
div.pack(fill=X, pady=2, padx=2)


# list tasks
drawAllTasks()

main_panel.pack(side=LEFT, fill=BOTH, expand=1)
border_panel.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()
