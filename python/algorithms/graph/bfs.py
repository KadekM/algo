import collections

from ads.graph.via_adj_list import Unidirected_graph

def bfs_distances_and_paths(g, u, v):
    distances = [None] * g.amount_of_vertices
    previous = [None] * g.amount_of_vertices
    queue, visited = collections.deque(), set()
    distances[u] = 0

    queue.append(u)
    visited.add(u)

    while len(queue) != 0:
        print(queue, visited)
        current = queue.popleft()

        for v in g.neighbours(current):
            if v not in visited:
                queue.append(v)
                visited.add(v)
                distances[v] = distances[current] + 1
                previous[v] = current



    return distances, previous




g = Unidirected_graph(7)
g.connect(0, 1)
g.connect(0, 2)
g.connect(0, 3)
g.connect(1, 2)
g.connect(1, 4)
g.connect(3, 4)
g.connect(4, 5)

print(g.adj)

distances, paths = bfs_distances_and_paths(g, 0, 2)
print(distances)
#decode path to 4:
prev = 5
path = []
while prev is not None:
    prev = paths[prev]
    path.append(prev)

print(path)


