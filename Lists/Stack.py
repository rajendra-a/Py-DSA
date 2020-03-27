# Stack in python is a linear data structure that stores items in Last in/First out
# or First in /Last out manner.
# In stack, a new element is added at one end and an element is removed at the same end only.
# The insert and delete operations are often called push and pop
# Unlike lists or arrays, random access is not allowed for the objects contained in the stack.

# The functions are associated with stack are 
# is_empty - Returns true if stack is empty, else false
# push - Adds an item in the stack
# pop - Removes an item from the stack
# peek - Returns the top element of the stack
# size - Returns the number of items in stack

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)


s = Stack()
s.push(2)
s.push(4)
s.push(6)
s.push(8)
s.push(10)

print(s)

print(s.is_empty())
print(s.peek())
s.push(12)
print(s.size())
print(s.is_empty())
print(s.pop())
print(s.pop())
print(s.size())
