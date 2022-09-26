class Heap():
    def _init__(self):
        self.data = []
    
    def get_root_node(self):
        return self.data[0]

    def get_last_node(self):
        return self.data[-1]
    
    def get_parent_index(self, index):
        return (index-1) // 2

    def get_left_child_index(self, index):
        return (index*2) + 1
    
    def get_right_child_index(self, index):
        return (index*2) + 2
    
    def insert(self,value):
        # Value becomes last node
        self.data.append(value)

        new_node_index = len(self.data)-1

        # If new node is not in root position and > parent
        while new_node_index > 0 and self.data[new_node_index] > self.data[self.get_parent_index(new_node_index)]:
            # Swap new node with parent
            self.data[self.get_parent_index(new_node_index)], self.data[new_node_index] \
            = self.data[new_node_index] ,  self.data[self.get_parent_index(new_node_index)]

            new_node_index = self.get_parent_index(new_node_index)

    def delete(self):
        # Only root can be deleted as a rule of Heap
        self.data[0] = self.data.pop()

        # Track the current index of "trickle node"
        trickle_node_index = 0

        # "trickle down" algo
        # Run loop until "trckle node" has a child > trickle
        while self.has_greater_child(trickle_node_index):
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)

            # Swap trickle node with larger child
            self.data[trickle_node_index], self.data[larger_child_index] = \
                self.data[larger_child_index], self.data[trickle_node_index]
            
            # Update trickle node's index
            trickle_node_index = larger_child_index

    def has_greater_child(self,index):
        # Checks whether the node at index has left and right child
        # and if either of those children > node at index
        (self.data[self.get_left_child_index(index)] and \
            self.data[self.get_left_child_index(index)] > self.data[index]) \
            or (self.data[self.get_right_child_index(index)] and \
            self.data[self.get_right_child_index(index)] > self.data[index])
    
    def calculate_larger_child_index(self,index):
        # if no right child
        if not(self.data[self.get_right_child_index]):
            return self.get_left_child_index(index)
        
        # If right child > left child
        if self.data[self.get_right_child_index(index)] > self.data[self.get_left_child_index(index)]:
            return self.get_right_child_index(index)
        else:
            return self.get_left_child_index(index)
        
