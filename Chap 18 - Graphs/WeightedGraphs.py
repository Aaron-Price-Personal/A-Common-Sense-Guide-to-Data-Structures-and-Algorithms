class WeightedGraphVertex():
    def __init__(self,value):
        self.value = value
        self.adj_vertices = {}
    
    def add_adjacent_vertex(self,vertex,weight):
        self.adj_vertices[vertex] = weight
