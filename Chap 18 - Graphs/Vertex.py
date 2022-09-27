class Vertex():
    def __init__(self,value):
        self.value = value
        self.adjacent_vertices = []
    
    # Use for directed graph
    def add_adjacent_vertex_dir(self,vertex):
        self.adjacent_vertices.append(vertex)

    # Use for undirected graph
    def add_adjacent_vertex_undir(self,vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex_undir(self)