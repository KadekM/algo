class Undirected_graph:
    def __init__(self, n):
        self.amount_of_vertices = n
        self.adj = [[False for _ in range(n)] for _ in range(n)]

    def connect(self, u, v):
        self.adj[u][v] = True
        self.adj[v][u] = True

    def disconnect(self, u, v):
        self.adj[u][v] = False
        self.adj[v][u] = False

    def neighbours(self, u):
        return [v for v, con in enumerate(self.adj[u]) if con]

    def is_edge(self, u, v):
        return self.adj[u][v] or self.adj[v][u]


class Undirected_graph_weighted:
    def __init__(self, n):
        self.amount_of_vertices = n
        self.adj = [[None for _ in range(n)] for _ in range(n)]

    def connect(self, u, v, w):
        self.adj[u][v] = w
        self.adj[v][u] = w

    def disconnect(self, u, v):
        self.adj[u][v] = None
        self.adj[v][u] = None

    def edge(self, u, v):
        return self.adj[u][v]

    def neighbours(self, u):
        return [(v, w) for v, w in enumerate(self.adj[u]) if w is not None]

    def is_edge(self, u, v):
        return self.adj[u][v] is not None or self.adj[v][u] is not None


class Directed_graph:
    def __init__(self, n):
        self.amount_of_vertices = n
        self.adj = [[False for _ in range(n)] for _ in range(n)]

    def connect(self, u, v):
        self.adj[u][v] = True

    def disconnect(self, u, v):
        self.adj[u][v] = False

    def neighbours(self, u):
        return [v for v, con in enumerate(self.adj[u]) if con]

    def is_edge(self, u, v):
        return self.adj[u][v]

    def transpose(self):
        self.adj = [list(x) for x in zip(*self.adj)]

