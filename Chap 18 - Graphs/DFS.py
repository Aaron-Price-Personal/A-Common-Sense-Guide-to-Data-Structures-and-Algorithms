def dfs_traverse(vertex,visited={}):
    visited[vertex.value] = True
    print(vertex.value)

    for adjacent in vertex.adjacent_vertices:
        if not(visited.get(adjacent.value)):
            dfs_traverse(adjacent,visited)

def dfs_search(vertex,toSearch,visited={}):
    if vertex.value == toSearch:
        return vertex
    
    visited[vertex.value] = True

    for adjacent in vertex.adjacent_vertices:
        if not(visited.get(adjacent.value)):

            if adjacent.value == toSearch:
                return adjacent
            
            vertex_searching_for = dfs_search(adjacent, toSearch, visited)
            if vertex_searching_for:
                return vertex_searching_for
    
    return None