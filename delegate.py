from Tkinter import *
import db
import TaskRow

root = Tk()

# --------------------
# FUNCTION DEFINITIONS
# --------------------
    
def drawCreateTaskButton():
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

def createTask():
    entryStr = StringVar()
    entryStr = taskEntry.get()
    taskEntry.delete(0, END)
    if len(entryStr) > 0:
        divisions = entryStr.split(";")

        divs = len(divisions)
        if(divs==1):
            db.createTask(divisions[0], "", "")
        elif(divs==2):
            db.createTask(divisions[0], divisions[1], "")
        else:
            db.createTask(divisions[0], divisions[1], divisions[2])
            
        #delete all tasks for redraw
        removeAllTaskRows()
        drawAllTasks()

def removeAllTaskRows():
    numTasks = len(root.taskRow)
    for r in xrange(0, numTasks):
        root.taskRow[r].delete()    
    
def drawAllTasks():
    numTasks = db.getNumTasks()
    root.taskRow = range(numTasks)
    curs = db.getAllTasks()
    r = 0
    for row in curs:
        root.taskRow[r] = TaskRow.TaskRow()
        root.taskRow[r].setFrame(bodyFrame)
        root.taskRow[r].setTitle(row[1])
        root.taskRow[r].setDesc(row[2])
        root.taskRow[r].createRow()
        r = r+1

    canvas.pack()

def drawTaskRow(r, c):
    root.taskRow[r] = TaskRow.TaskRow()
    root.taskRow[r].setFrame(c)
    root.taskRow[r].setTitle("Brian"+str(r))
    root.taskRow[r].setID(r)
    root.taskRow[r].createWidgets()
    root.taskRow[r].draw()

# ---------
# GUI STUFF
# ---------

root.title("Delegate")
root.geometry("800x600")
btn_side = range(4)

containerFrame = Frame(root)
containerFrame.config(bg="#e8e8e8", pady=10, padx=2, width=900)
containerFrame.pack(fill=BOTH, expand=1)


# -----------------
# CREATE SIDE PANEL
# -----------------
sidePanel = Frame(containerFrame)
sidePanel.config(bg="#e8e8e8")

# Options pulled from sort_options
sort_label = Label(sidePanel, text="Sort By:", font=("Arial", 8))
sort_label.config(bg="#e8e8e8")
sort_label.pack(side=TOP, fill=X)

div = Frame(sidePanel)
div.config(bg="#ffffff", height=1, relief=FLAT)
div.pack(fill=X, pady=2, padx=2)

c = db.getSortNames()
r=0
for row in c:
    btn_side[r] = Button(sidePanel, text=row[0])
    btn_side[r].config(anchor=W, relief=FLAT, bg="#e8e8e8")
    btn_side[r].pack(side=TOP, fill=X)

    div = Frame(sidePanel)
    div.config(bg="#ffffff", height=1, relief=FLAT)
    div.pack(fill=X, pady=2, padx=2)

    r = r+1

btn_side[0].config(bg="#afcefc")

# TODO
# Filter options

sidePanel.pack(side=LEFT, fill=BOTH)

# -----------------
# CREATE MAIN PANEL
# -----------------

containerFrame.grid_rowconfigure(0, weight=1)
containerFrame.grid_columnconfigure(0, weight=1)

canvas = Canvas(containerFrame)
scrollbar = Scrollbar(containerFrame, orient=VERTICAL)

scrollbar.config(command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.pack(side=TOP, fill=X, expand=1, anchor=N)
        
canvas.config(scrollregion=canvas.bbox(ALL))
bodyFrame = Frame(canvas, padx=1, pady=1)
bodyFrame.config(bg="#cbcbcb")
bodyFrame.pack(side=TOP, fill=X, expand=1)
canvas.create_window(0,0, window=bodyFrame, anchor="nw")

# Create New Task
newTask = Frame(bodyFrame)
newTask.config(bg="#e8e8e8")
newTask.pack(side=TOP, fill=X, expand=0, anchor=N)

taskEntry = Entry(newTask)
taskEntry.config(bg="#ffffff", relief=FLAT)
taskEntry.pack(side=LEFT, fill=BOTH, expand=1)
taskEntry.insert(0,"Add New Task")

taskButton = Button(newTask)
taskButton.config(text=">>>", relief=FLAT, command=createTask)
taskButton.pack(side=RIGHT, fill=X, expand=0)

newTaskBorder = Frame(bodyFrame)
newTaskBorder.config(height=2, bg="#cbcbcb")
newTaskBorder.pack(side=TOP, fill=X, expand=1)


numTasks = db.getNumTasks()

if numTasks > 0:
    root.taskRow = range(numTasks)
    data = db.getAllTasks()
    r = 0
    for row in data:
        root.taskRow[r] = TaskRow.TaskRow()
        root.taskRow[r].setFrame(bodyFrame)
        root.taskRow[r].setTitle(row[1])
        root.taskRow[r].setDesc(row[2])
        root.taskRow[r].createRow()
        
        r = r+1
else:
    emptyTasks = Frame(bodyFrame)
    emptyTasks.config(bg="#ffffff")
    emptyTasks.pack(side=TOP, fill=BOTH, expand=1)
    
##taskRow = range(10)
##for r in xrange(0,9):
##    taskRow[r] = TaskRow.TaskRow()
##    taskRow[r].setFrame(bodyFrame)
##    taskRow[r].createRow()


bodyFrame.pack(side=TOP, fill=X, expand=1)

canvas.config(scrollregion=canvas.bbox(ALL))


root.mainloop()
