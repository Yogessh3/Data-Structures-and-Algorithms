'''Double Ended Queue Implementation'''
class deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
dq=deque()
dq.addFront(1)
dq.addRear(2)
dq.addFront(3)
print(dq.removeFront())
dq.addFront(4)
dq.addRear(5)
print(dq.removeFront())
print(dq.removeRear())  
