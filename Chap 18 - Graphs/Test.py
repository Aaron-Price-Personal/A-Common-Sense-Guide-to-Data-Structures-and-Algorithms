from Vertex import Vertex
import DFS, BFS

alice,bob, candy = Vertex("alice") , Vertex("bob"), Vertex("candy")
derek, elaine, fred = Vertex("derek"), Vertex("elaine"), Vertex("fred")
gina, helen, irena = Vertex("gina"), Vertex("helen"), Vertex("irena")

alice.add_adjacent_vertex_undir(bob)
alice.add_adjacent_vertex_undir(candy)
alice.add_adjacent_vertex_undir(derek)
alice.add_adjacent_vertex_undir(elaine)

bob.add_adjacent_vertex_undir(fred)

candy.add_adjacent_vertex_undir(helen)

derek.add_adjacent_vertex_undir(elaine)
derek.add_adjacent_vertex_undir(gina)

fred.add_adjacent_vertex_undir(helen)

gina.add_adjacent_vertex_undir(irena)

DFS.dfs_traverse(alice)
DFS.dfs_search(alice,"fred")
print()
BFS.bfs_traverse(alice)