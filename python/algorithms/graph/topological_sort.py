from ads.graph.via_adj_list import Directed_graph


def topological_sort(g):
    visited = set() # or could be array of booleans or something...
    result = []

    def visit(u):
        visited.add(u)

        for v in g.neighbours(u):
            if v not in visited:
                visit(v)

        result.append(u)

    vertices = range(g.amount_of_vertices)
    for u in vertices:
        if u not in visited:
            visit(u)

    return result



g = Directed_graph(7)
g.connect(0, 1)
g.connect(0, 2)
g.connect(0, 3)
g.connect(1, 2)
g.connect(1, 4)
g.connect(3, 4)
g.connect(4, 5)

print(topological_sort(g))
