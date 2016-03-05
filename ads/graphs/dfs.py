from ads.graphs.representation.list import Unidirected_graph
import collections

def dfs(g, start):
    visited = set()
    previous = [None] * g.amount_of_vertices

    def visit(u):
        visited.add(u)

        for v in g.neighbours(u):
            if v not in visited:
                previous[v] = u
                visit(v)

    visit(start)
    return previous




g = Unidirected_graph(7)
g.connect(0, 1)
g.connect(0, 2)
g.connect(0, 3)
g.connect(1, 2)
g.connect(1, 4)
g.connect(3, 4)
g.connect(4, 5)

print dfs(g, 0)
