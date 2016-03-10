from ads.graph.via_adj_matrix import *

x = Undirected_graph(5)
x.connect(2,4)
x.connect(2,1)
print(x.is_edge(1,2))
print(x.neighbours(2))

x = Undirected_graph_weighted(5)
x.connect(2,4, 94)
x.connect(2,1, 55)
print(x.neighbours(2))
print(x.edge(1,2))


A = Directed_graph(5)
A.connect(0,1)
A.connect(1,2)
A.connect(2,0)
A.connect(1,3)
A.connect(3,4)
A.connect(4,3)
print(A.adj)
A.transpose()
print(A.adj)

