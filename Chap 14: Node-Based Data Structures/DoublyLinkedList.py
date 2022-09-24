class Node():
    def __init__(self,data,next_node=None,prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class DoublyLinkedList():
    def __init__(self,first_node=None,last_node=None):
        self.first_node = first_node
        self.last_node = last_node
    
    def insert_at_end(self,value):
        new_node = Node(value)

        if not(self.first_node):
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.prev_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node
    
    def remove_from_front(self):
        removed_node = self.first_node
        self.first_node = self.first_node.next_node
        return removed_node
    
    def printAllReverse(self):
        current_node = self.last_node

        while current_node:
            print(current_node.data)

            current_node = self.last_node.prev_node

class Queue():
    def __init__(self,data):
        self.data = DoublyLinkedList()
    
    def enqueue(self,element):
        self.data.insert_at_end(element)
    
    def dequeue(self):
        removed_node = self.data.remove_from_front
        return removed_node.data
    
    def read(self):
        if not(self.data.first_node):
            return None
        return self.data.first_node.data
