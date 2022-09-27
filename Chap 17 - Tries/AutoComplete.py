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
    
    def traverse(self,node=None):
        current_node = node or self.root

        for key, childNode in current_node.children.items():
            print(key)
            if key != "*":
                self.traverse(childNode)
    
    def autocorrect(self, word):
        currentNode = self.root

        # Keep track of how much of the user's word we have found
        wordFoundSoFar = ""

        for char in word:
            # If the current node has child key with current char
            if currentNode.children.get(char):
                wordFoundSoFar += char
                # Follow child node
                currentNode = currentNode.children.get(char)

            else:
                # If current char not found
                # collect all suffixes wit hte prefix weve found
                # Concatenate word foudn so far with ending of valid word
                # to suggest the wrod the user meant to type in
                return wordFoundSoFar + self.collectAllWords(currentNode)[0]
        
        # If the user's word is found in the trie
        return word