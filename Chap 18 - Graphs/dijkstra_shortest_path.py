def dijkstras_shortest_path(starting_vertex, final_vertex):
    cheapest_prices_table = {}
    cheapest_previous_vertex_table = {}

    unvisited_vertices= []
    visited_vertices= {}

    cheapest_prices_table[starting_vertex.value] = 0
    current_vertex = starting_vertex

    # Main algorithm loop
    while current_vertex:
        visited_vertices[current_vertex.value] = True
        unvisited_vertices.remove(current_vertex)

        for adj_vertex,cost in current_vertex.adj_vertices.items():
            # If discovered a new vertex we add to unvisited vertex array
            if not visited_vertices[adj_vertex.value]:
                unvisited_vertices.append(adj_vertex)
            
            # Calculate cost of getting from Start to Adj vertex via current
            # vertex as second to last stop
            cost_through_current_vertex = cheapest_prices_table[adj_vertex.value] + cost

            # Check wheteher cost is cheaper from starting to Adj vertex
            if not(cheapest_prices_table[adj_vertex.value]) \
            or cost_through_current_vertex < cheapest_prices_table[adj_vertex.value]:
                # update tables
                cheapest_prices_table[adj_vertex.value] = cost_through_current_vertex
                cheapest_previous_vertex_table[adj_vertex.value] = current_vertex.value
        
        # Visit next unvisited vertex. Choose cheapest path from START
        current_vertex = cheapest_prices_table[min(unvisited_vertices).value]
    
    # Calculate precise path
    shortest_path = []

    # Work backwards from final dest to start
    current_vertex_value = final_vertex.value

    while current_vertex_value != starting_vertex.value:
        shortest_path.append(current_vertex_value)

        #Use cheapest_prev_vert_tab to follow each vertex via key pair values to previous vertex
        current_vertex_value = cheapest_previous_vertex_table[current_vertex_value]
    
    shortest_path.append(starting_vertex.value)

    return shortest_path.reverse()
