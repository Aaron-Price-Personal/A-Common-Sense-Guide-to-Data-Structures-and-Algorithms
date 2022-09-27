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
    
    def collectAllWords(self,node = None, word = "", words=[]):
        current_node = node or self.root

        for key, childNode in current_node.children.items():
            # If key = * then we have hit end of word
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(childNode, word + key, words)
        
        return words
    
    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords(currentNode)
