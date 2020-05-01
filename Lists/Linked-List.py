""" there is no Linked list type data structure in python
    we are going to use classes that represent data structures"""

""" To initialise new element"""
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

""" To create new linked list"""
class LinkedList(object):
    def __init__(self, head):
        self.head = head
        self.size = 0

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current=current.next
                current.next=new_element
        else:
            self.head = new_element
        self.size += 1
    
    def insert(self, position, new_element):
        self.size += 1
        current = self.head
        counter = 1
        if position < 1:
            return None
        while current and counter < position:
            if counter == position - 1
                new_element.next = current.next
                current.next = new_element
            current = current.next
            counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
    
    def size(self):
        return self.size

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None


    def delete(self, element):
        self.size -= 1
        current = self.head
        previous = None
        while current.value != element and current.next:
            previous = current
            current = current.next

        if current.value == element:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

