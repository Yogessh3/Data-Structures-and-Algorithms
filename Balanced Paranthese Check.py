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
def brackets_check(string):
    if(len(string)%2!=0):
        return False
    else:
        s=stack()
        opening={'(','{','['}
        matching={('(',')'),('{','}'),('[',']')}
        for paren in brackets:
            if paren in opening:
                s.push(paren)
            else:
                if(s.size()==0):
                    return False
                top_element=s.pop()
                if (top_element,paren) not in matching:
                    return  False
        return s.size()==0            
brackets=input()
print(brackets_check(brackets))

        
