""" there is no Linked list type data structure in python
    we are going to use classes that represent data structures"""


class Element(object):
    """ To initialise new element"""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    """ To create new linked list"""
    def __init__(self, head):
        self.head = head
        self.size = 0

    def append(self, new_element):
        """To append new element at the end of the Linkedlist"""
        current = self.head
        if self.head:
            while current.next:
                current=current.next
                current.next=new_element
        else:
            self.head = new_element
        self.size += 1
    
    def insert(self, position, new_element):
        """ To insert in a particular position """
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
        """ To get the size of the linkedlist """
        return self.size

    def get_position(self, position):
        """ To get the position of the element in linked list """
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
        """ To delete an element from the linkedlist """
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

