import queue

def bfs_traverse(starting_vertex):
    q = queue.Queue()

    visited = {}
    visited[starting_vertex.value] = True
    q.put(starting_vertex)

    while not q.empty():
        current_vertex = q.get()

        print(current_vertex.value)

        for adjacent in current_vertex.adjacent_vertices:
            if not(visited.get(adjacent.value)):
                visited[adjacent.value] = True

                q.put(adjacent)

def bfs_search(vertex, to_search):
    q = queue.Queue()
    visited = {}
    visited[vertex.value] = True

    while not q.empty():
        current_vertex = q.get()
        if adjacent.value == to_search:
                    return adjacent

        for adjacent in current_vertex.adjacent_vertices:
            if not(visited.get(adjacent.value)):
                visited[adjacent.value] = True
                q.put(adjacent)
    
    return None