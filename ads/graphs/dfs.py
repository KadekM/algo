from ads.graphs.representation.list import Unidirected_graph
import collections

def dfs(g, start):
    visited = set()
    previous = [None] * g.amount_of_vertices
    enter = [None] * g.amount_of_vertices
    leave = [None] * g.amount_of_vertices
    time = 0

    def visit(u):
        nonlocal time

        visited.add(u)
        time += 1
        enter[u] = time

        for v in g.neighbours(u):
            if v not in visited:
                previous[v] = u
                visit(v)

        time += 1
        leave[u] = time

    visit(start)
    return previous, list(zip(enter, leave))




g = Unidirected_graph(7)
g.connect(0, 1)
g.connect(0, 2)
g.connect(0, 3)
g.connect(1, 2)
g.connect(1, 4)
g.connect(3, 4)
g.connect(4, 5)

print(dfs(g, 0))
