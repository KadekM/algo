class Unidirected_graph:
    def __init__(self, n):
        self.amount_of_vertices = n
        self.adj = [[] for _ in range(n)] # could be set

    def connect(self, u, v):
        self.adj[u].append(v) # careful with duplicates, when list
        self.adj[v].append(u)

    def disconnect(self, u, v):
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def neighbours(self, u):
        return self.adj[u]

    def is_edge(self, u, v):
        return v in self.adj[u] or u in self.adj[v]


class Directed_graph:
    def __init__(self, n):
        self.amount_of_vertices = n
        self.adj = [[] for _ in range(n)] # could be set

    def connect(self, u, v):
        self.adj[u].append(v) # careful with duplicates, when list

    def disconnect(self, u, v):
        self.adj[u].remove(v)

    def neighbours(self, u):
        return self.adj[u]

    def is_edge(self, u, v):
        return v in self.adj[u]

    def tranpose(self):
        adjT = [[] for _ in range(self.amount_of_vertices)]
        for u, xs in enumerate(self.adj):
            for v in xs:
                adjT[v].append(u)
        self.adj = adjT


# Weights is seperate dict, but weight could be stored in node
class Unidirected_graph_weighted:
    def __init__(self, n):
        self.amount_of_vertices = n
        self.adj = [[] for _ in range(n)] # could be set
        self.weights = {}

    def connect(self, u, v, w):
        self.adj[u].append(v) # careful with duplicates, when list
        self.adj[v].append(u)
        self.weights[(u,v)] = w
        self.weights[(v,u)] = w

    def disconnect(self, u, v):
        self.adj[u].remove(v)
        self.adj[v].remove(u)
        del self.weights[(u,v)]
        del self.weights[(v,u)]

    def edge(self, u, v):
        return self.weights[(u,v)]

    def neighbours(self, u):
        return [(v, self.weights[u,v]) for v in self.adj[u]]

    def is_edge(self, u, v):
        return (u,v) in self.weights


#g = Unidirected_graph(5)
#g.connect(1,2)
#print(g.is_edge(3,1))
#g.connect(3,2)
#print(g.is_edge(3,2))

#g = Unidirected_graph_weighted(5)
#g.connect(1,2, 55)
#print(g.is_edge(3,1))
#g.connect(3,2, 95)
#print(g.edge(3,2))
#print(g.neighbours(2))
