class queue:
    def __init__(self):
        self.instack=[]
        self.outstack=[]
    def enqueue(self,item):
        self.instack.append(item)
    def dequeue(self):
        if self.outstack==[]:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())        
