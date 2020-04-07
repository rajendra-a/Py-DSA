# It close to stack 
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        data = self.items[0]
        del self.items[0]
        return data 

    def peek(self):
        return self.queue[0]
    
    def size(self):
        return len(self.items)

q = Queue()
q.enqueue(10)
q.enqueue(4)
q.enqueue(20)

q.dequeue()

print(q.size())
print(q.is_empty())