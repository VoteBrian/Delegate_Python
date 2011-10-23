from Tkinter import *

class TaskRow():
    _title = "Default"
    _desc = "Default"
    
    _id = 0

    def setFrame(self, frame):
        self._frame = frame
    
    def setID(self, id):
        self._id = id
        
    def setTitle(self, title):
        self._title = title

    def setDesc(self, desc):
        self._desc = desc

    def setAssignee(self, assignee):
        self._assignee = assignee

    def createRow(self):
        self.frameRow = Frame(self._frame)
        self.frameRow.config(bg="#d9d9d9")
        self.frameRow.pack(side=TOP, fill=X, expand=1, anchor=N)

        self.frameTitle = Label(self.frameRow, font=("Arial", 12), padx=10)
        self.frameTitle.config(bg="#ffffff", text=self._title, anchor=W)
        self.frameTitle.pack(side=TOP, fill=X, expand=0)

        self.frameDesc = Label(self.frameRow, font=("Arial", 8), padx=10)
        self.frameDesc.config(bg="#ffffff", fg="#555555", text=self._desc, anchor=W)
        self.frameDesc.pack(side=TOP, fill=BOTH, expand=1)

        self.rowBorder = Frame(self.frameRow, padx=10)
        self.rowBorder.config(height=1, relief=FLAT, bg="#cbcbcb")
        self.rowBorder.pack(side=TOP, fill=X, expand=1)

    def delete(self):
        self.frameRow.destroy()
        self.frameTitle.destroy()
        self.frameDesc.destroy()
        self.rowBorder.destroy()
