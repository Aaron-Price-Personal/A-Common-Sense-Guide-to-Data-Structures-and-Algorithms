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

    def print_all(self):
        current_node = self.first_node

        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
    
    def get_last(self):
        current_node = self.first_node

        while current_node:
            if current_node.next_node == None:
                return current_node.data
            current_node = current_node.next_node
        return None
    
    def reverse_list(self):
        prev_node = None
        current_node = self.first_node

        while current_node:
            next_node = current_node.next_node

            current_node.next_node = prev_node

            prev_node = current_node
            current_node = next_node
        
        self.first_node = prev_node
    
    def delete_mid_node(self,node):
        node.data = node.next_node.data
        node.next_node = node.next_node.next_node


'''
Code below allows to try out data structure

node_1 = Node("a")
node_2 = Node("b")
node_3 = Node("c")
node_4 = Node("d")

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

linked_list = LinkedList(node_1)

print(linked_list.read(3))
print(linked_list.search("a"))
linked_list.print_all()
print(linked_list.get_last())
linked_list.reverse_list()
linked_list.print_all()
'''