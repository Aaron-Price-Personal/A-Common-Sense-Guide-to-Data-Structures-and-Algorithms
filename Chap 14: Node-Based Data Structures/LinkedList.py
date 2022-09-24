class Node():
    def __init__(self,data,next_node=None):
        self.data = data
        self.next_node = next_node
    
class LinkedList():
    def __init__(self,first_node):
        self.first_node = first_node
    
    def read(self,index):
        # First node of list
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            current_node = current_node.next_node
            current_index += 1

            if not(current_node):
                return None
        
        return current_node.data
    
    def search(self,value):
        current_node = self.first_node
        current_index = 0

        while current_node:
            if current_node.data == value:
                return current_index
            
            # Otherwise move to nxt node

            current_node = current_node.next_node
            current_index += 1
        
        return None
    
    def insert_at_index(self,index,value):
        new_node = Node(value)

        # Inserting at the beggining of list
        if index == 0:
            new_node.next_node = self.first_node

            self.first_node = new_node
            return
        
        # Inserting anyhwere else
        current_node = self.first_node
        current_index = 0

        # Access node before immediatly before where new node will be added
        while current_index < (index-1):
            current_node = current_node.next_node
            current_index += 1
        
        # Have new node link to next node
        new_node.next_node = current_node.next_node

        # Modify link of previous node to point to new node
        current_node.next_node = new_node
    
    def delete_at_index(self,index):
        if index == 0:
            self.first_node = self.first_node.next_node
            return

        current_node = self.first_node
        current_index = 0

        # Find node before the one we want to delete and cull current node
        while current_index < (index-1):
            current_node = current_node.next_node
            current_index += 1
        
        # Find node that comes after the one we delete
        node_after_deleted = current_node.next_node.next_node

        # Change link of current node to point to node after one we want delted
        current_node.next_node = node_after_deleted


    