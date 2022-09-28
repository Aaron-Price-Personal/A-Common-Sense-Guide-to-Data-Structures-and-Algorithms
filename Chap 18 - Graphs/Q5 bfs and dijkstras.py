import queue

'''
Thew algorithm finds the shortest path of an unweighted graph
it used BFS and dijkstras algorithm 
efficiency: O(V^2)
Uses: Social media finding how close a connection is e.g first, second ... etc
'''
def shortest_path_unweighted(starting_vertex,vertex_to_find,visited = {}):
    q = queue.Queue()
    prev_vertex_table = {}
    visited[starting_vertex.value] = True
    q.put(starting_vertex)

    while not q.empty():
        current_vertex = q.get()

        for adjacent in current_vertex.adjacent_vertices:
            if not(visited.get(adjacent.value)):
                visited[adjacent.value] = True
                q.put(adjacent)

                prev_vertex_table[adjacent.value] = current_vertex.value

    # Dijkstras now works backwards to find our shortest path
    shortest_path = []
    current_vertex_value = vertex_to_find.value

    while current_vertex_value != starting_vertex.value:
        shortest_path.append(current_vertex_value)
        current_vertex_value = prev_vertex_table[current_vertex_value]

    shortest_path.append(starting_vertex.value)

    return shortest_path.reverse       