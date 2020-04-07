""" there is no Linked list type data structure in python
    we are going to use classes that represent data structures"""

""" To initialise new element"""
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head):
        self.head = head
    
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current=current.next
                current.next=new_element
        else:
            self.head = new_element
    
    def insert(slef, position, new_element):
        current = self.head
        counter = 1
        if position < 1:
            return None
        while current and counter <= position:
            return current
    