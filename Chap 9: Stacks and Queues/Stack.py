class Stack():
    def __init__(self):
        self.data = []
    
    def push(self,element):
        return self.data.append(element)
    
    def pop(self):
        return self.data.pop()
    
    def read(self):
        return self.data[-1]

