class stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,element):
        self.items.append(element)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
s=stack()
print(s.isEmpty())
arr=[1,2,3,4,5,6]
for i in arr:
    s.push(i)
print(s.peek())
print(s.pop())
print(s.size())
print(s.isEmpty())
