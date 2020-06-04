class queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())       
