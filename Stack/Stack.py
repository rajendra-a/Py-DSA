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

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass
    

class Stack:
    """LiFO stack implementation using python list as underlying storage"""

    def __init__(self):
        """Crate an empty stack"""
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        """ Add element to the top of the stack"""
        self.items.append(item) # new item stored at the end of the list
    
    def pop(self):
        """ Remove and return element from the top of the stack"""
        """Raise Empty exception if the stack is empty"""
        if self.is_empty():
            raise Empty("stack is empty")
        return self.items.pop() # remove last item from the list
    
    def peek(self):
        """Return the top element of the stack"""
        """Raise Empty exception if the stack is empty"""
        if self.is_empty():
            raise Empty("stack is empty")
        return self.items[-1] # the last item in the list 
    
    def size(self):
        """Return the number of elements in the stack"""
        """ Raise the Empty exception is the stack is empty"""
        if self.is_empty():
            raise Empty("stack is empty")
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
