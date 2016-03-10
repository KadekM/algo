from ads.graph.via_adj_matrix import *
import copy


def kosaraju(g):

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

    #print(stack)

    # second visit on transpose matrix

    gg = copy.copy(g)
    gg.transpose()

    visited = [False] * gg.amount_of_vertices
    groups = [-1] * gg.amount_of_vertices

    def dfsT(current, groupId):
        visited[el] = True
        groups[el] = groupId

        for v in gg.neighbours(current):
            if not visited[v]:
                visited[v] = True
                groups[v] = groupId
                dfsT(v, groupId)

    groupId = 0
    while len(stack) > 0:
        el = stack.pop()
        if visited[el]: continue
        dfsT(el, groupId)
        groupId += 1

    return groups

def tarjan(g):
    pass
