class Queue():
    def __init__(self):
        self.data = []
    
    def enqueue(self,element):
        self.data.append(element)
    
    def dequeue(self):
        del self.data[0]
    
    def read(self):
        return self.data[0]