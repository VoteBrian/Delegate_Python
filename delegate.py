from Tkinter import *
import db
import TaskRow

root = Tk()

# initialize database and tables
#db.initialize()

# --------------------
# FUNCTION DEFINITIONS
# --------------------

def createTask():
    s = StringVar()
    s = new_task_entry.get()
    new_task_entry.delete(0, END)
    if len(s) > 0:
        db.createTask(s)

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
        root.taskRow[r].setFrame(main_panel)
        root.taskRow[r].setTitle(row[1])
        root.taskRow[r].setID(row[0])
        root.taskRow[r].createWidgets()
        root.taskRow[r].draw()
        r = r+1



# ---------
# GUI STUFF
# ---------
#root = Tk()
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

# TODO
# Filter options

sidePanel.pack(side=LEFT, fill=BOTH)

# -----------------
# CREATE MAIN PANEL
# -----------------

# canvas for scrolling
##container_Frame.grid_rowconfigure(0, weight=1)
##container_Frame.grid_columnconfigure(0, weight=1)
##
##yscrollbar = Scrollbar(container_Frame)
##yscrollbar.grid(row=0, column=1, sticky=N+S)
##
##canvas = Canvas(container_Frame, yscrollcommand=yscrollbar.set)
##canvas.pack(side=LEFT, fill=BOTH, expand=1)

# border
border_panel = Frame(container_Frame)
border_panel.config(bg="#cbcbcb", padx=1, pady=1)
border_panel.pack(side=LEFT, fill=BOTH, expand=1)

# content
main_panel = Frame(border_panel)
main_panel.config(bg="#ffffff")
main_panel.pack(side=LEFT, fill=BOTH, expand=1)

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

root.mainloop()
