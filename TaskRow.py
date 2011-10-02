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

    def createWidgets(self):
        self.titleBtn = Checkbutton(self._frame, text=self._title)
        self.div = Frame(self._frame)

    def draw(self):
        self.titleBtn.config(bg="#ffffff", anchor=W, relief=FLAT)
        self.titleBtn.pack(side=TOP, fill=X)
        
        self.div.config(height=2, bd=1, relief=SUNKEN)
        self.div.pack(fill=X, pady=2, padx=2)

    def delete(self):
        self.titleBtn.destroy()
        self.div.destroy()
    
