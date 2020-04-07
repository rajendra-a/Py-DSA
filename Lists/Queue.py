# It close to stack, as a queue is collection of objects that are inserted and removed
# according to the firt in first out FIFO.
# That is elements can be inserted at any time but the element that has been in the queue
# the longest can be next removed.

# we usually say that elements enter a queue at the back and are removed from from the front

class Empty(Exception):
    """Error attempting to access an element from empty queue"""
    pass

class Queue:
    """FIFO Queue implementation using python list as underlying storage"""
    def __init__(self):
    """ Create an empty Queue """
        self.items = []
    
    def is_empty(self):
        """Return True if the Queue is empty"""
        return self.items == []

    def enqueue(self, item):
        """Add an element to the back of the Queue"""
        self.items.append(item) # add element to end of the list
    
    def dequeue(self):
        """Remove and return the front element of the queue"""
        """Raise empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.items.pop(0) 

    def First(self):
        """ Return the element at the front of the queue"""
        """ Raise Empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.queue[0] # returning the first element of the list
    
    def last(self):
        """Return the element at the back of the queue"""
        """Raise Empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.queue[-1] # Return the last element in the list
    
    def size(self):
        """Return the number of elements in the queue"""
        """Raise the Empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return len(self.items)

q = Queue()
q.enqueue(10)
q.enqueue(4)
q.enqueue(20)

q.dequeue()

print(q.size())
print(q.is_empty())