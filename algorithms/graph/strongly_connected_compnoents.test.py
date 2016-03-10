from ads.graph.via_adj_matrix import Directed_graph
from algorithms.graph.strongly_connected_components import *

Z = Directed_graph(3)
Z.connect(0, 1)
Z.connect(1, 2)
Z.connect(2, 1)
print(kosaraju(Z))

A = Directed_graph(5)
A.connect(0,1)
A.connect(1,2)
A.connect(2,0)

A.connect(1,3)
A.connect(3,4)
A.connect(4,3)

print(kosaraju(A))


B = Directed_graph(8)
B.connect(0,1)
B.connect(1,2)
B.connect(2,1)

B.connect(3,4)
B.connect(4,5)
B.connect(5,3)

B.connect(6,7)

print(kosaraju(B))
