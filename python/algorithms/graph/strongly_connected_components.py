from ads.graph.via_adj_matrix import *
from copy import *


# https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
# O(V^2) when adj.matrix, O(E+V) when adj.list
def kosaraju(g):

    # Build stack of vertices when leaving
    stack = []
    visited = [False] * g.amount_of_vertices

    def dfs(current):
        for v in g.neighbours(current):
            if not visited[v]:
                visited[v] = True
                dfs(v)
        stack.append(current)

    for i in range(g.amount_of_vertices):
        if not visited[i]:
            visited[i] = True
            dfs(i)


    # Second visit on transpose matrix (edges reversed)
    gg = copy(g)
    gg.transpose()

    # Reset visited
    visited = [False] * gg.amount_of_vertices
    groups = []

    def dfsT(current):
        gr = [current]

        for v in gg.neighbours(current):
            if not visited[v]:
                visited[v] = True
                gr += dfsT(v)
        return gr

    while len(stack) > 0:
        el = stack.pop()
        if not visited[el]:
            visited[el] = True
            next_group = dfsT(el)
            groups.append(next_group)

    return groups

def tarjan(g):
    pass
