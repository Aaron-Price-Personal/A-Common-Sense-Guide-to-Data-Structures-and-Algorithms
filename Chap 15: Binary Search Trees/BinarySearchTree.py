class TreeNode():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.leftChild = left
        self.rightChild = right

def search(searchVal, node):
    # Base case: Node = non existent or searchVal
    if node is None or node.data == searchVal:
        return node
    
    # If val < node search left
    elif searchVal < node.data:
        return search(searchVal,node.leftChild)
    elif searchVal > node.data:
        return search(searchVal, node.rightChild)

def insert(value, node):
    if value < node.data:
        # If no current left child insert value
        if node.leftChild is None:
            node.leftChild.data = value
        else:
            insert(value,node.leftChild)
    
    elif value > node.data:
        # If no current right child insert value
        if node.rightChild is None:
            node.rightChild.data = value
        else:
            insert(value,node.rightChild)
        
def delete(valueToDel,node):
    # Base Case: bottom of tree, parent has no child
    if node is None:
        return None
    
    # If value deleting < or > current node we set
    # left or right respectivly to return val of a recursive call
    # onto node's left or right subtree
    elif valueToDel < node.data:
        node.leftChild = delete(valueToDel,node.leftChild)

        # Returned curret node to be used as new value of its parent's left or right
        return node
    elif valueToDel > node.data:
        node.rightChild = delete(valueToDel, node.leftChild)
        return node
    elif valueToDel == node.data:
        # If no left child delete via returning right child to be new subtree
        if node.leftChild is None:
            return node.rightChild

            # if no left or right then we have base case
        elif node.rightChild is None:
            return node.leftChild
        
        # If two children, del current node vai lift()
        # This will change current node's value to successor node
        else:
            node.rightChild = lift(node.rightChild,node)

def lift(node,nodeToDelete):
    # If current node has left child, continue down left to find successor
    if node.leftChild:
        node.leftChild = lift(node.leftChild,nodeToDelete)
        return node # Successor node
    
    # If no left child, then current node = successor node
    # Therefor take its value and make it new value of deleted nodes place
    else:
        return node.rightChild

def traverse_and_print(node):
    if node is None:
        return
    traverse_and_print(node.leftChild)
    print(node.data)
    traverse_and_print(node.rightChild)
