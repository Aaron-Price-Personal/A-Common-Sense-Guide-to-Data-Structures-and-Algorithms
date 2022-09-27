class TrieNode():
    def __init__(self):
        self.children = {}

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def search(self,word):
        currentNode = self.root

        for char in word:
            # If the current node has child key with char
            if currentNode.children.get(char):
                # Follow child node
                currentNode = currentNode.children[char]
            else:
                # If the current char isnt found word cant exist
                return None
        
        return currentNode

    def insert(self,word):
        currentNode = self.root

        for char in word:
            # If the current node has child key with char
            if currentNode.children.get(char):
                # Follow child node
                currentNode = currentNode.children[char]
            else:
                # If the current char isnt found add char to children
                newNode = TrieNode()
                currentNode.children[char] = newNode

                currentNode = newNode
        
        currentNode.children["*"] = None
        
        return currentNode