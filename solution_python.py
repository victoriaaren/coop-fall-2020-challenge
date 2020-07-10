class EventSourcer():
    # Do not change the signature of any functions
    
    def __init__(self):
        self.value = 0
        self.undoStack = []
        self.redoStack = []

    def add(self, num: int):
        self.value=self.value+num
        self.undoStack.append(self.value)
        return self.value

    def subtract(self, num: int):
        self.value-=num
        self.undoStack.append(self.value)
        return self.value

    def undo(self):
      if(len(self.undoStack)>0):
        self.redoStack.append(self.undoStack.pop())
        self.value = self.undoStack[len(self.undoStack) -1]
      return self.value


    def redo(self):
        if(len(self.redoStack) >0):
          self.undoStack.append(self.redoStack.pop())
          self.value = self.undoStack[len(self.undoStack) -1]
        return self.value

    def bulk_undo(self, steps: int):
        if(len(self.undoStack)>=steps):
          for i in range(steps):
            self.redoStack.append(self.undoStack.pop())
          self.value = self.undoStack[len(self.undoStack)-1]
        return self.value

    def bulk_redo(self, steps: int):
      if(len(self.redoStack)>=steps):
        for i in range(steps):
          self.undoStack.append(self.redoStack.pop())
        self.value = self.undoStack[len(self.undoStack)-1]
      return self.value
