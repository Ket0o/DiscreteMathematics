import matplotlib
import igraph as ig
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
import string
import numpy
matplotlib.use('TkAgg')

def Update_graph(G, nodes, edges):
    G.clear()
    rnd.shuffle(nodes)
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

G = nx.Graph()

print("Введите n:")
n = int(input())

nodes = []
edges = []
stroka = ""
vector = rnd.random_integers(0, 2, size=(n, n))

for i in range(0, n):
    nodes.append(string.ascii_uppercase[i])

mas = numpy.tril(vector) + numpy.tril(vector, -1).T

for i in range (n):
    stroka = stroka + string.ascii_uppercase[i] + " "
print("  ", stroka)

for i in range (n):
    print(string.ascii_uppercase[i], mas[i])

for i in range(0, n):
    for j in range(i, n):
        if (mas[i, j] == 0):
            continue
        if (mas[i, j] == 1):
            edges.append((string.ascii_uppercase[i], string.ascii_uppercase[j]))
        if (mas[i, j] == 2):
            edges.append((string.ascii_uppercase[i], string.ascii_uppercase[j]))
            edges.append((string.ascii_uppercase[j], string.ascii_uppercase[i]))

G.add_nodes_from(nodes)
print(edges)
G.add_edges_from(edges)

print()
print(G.nodes())
print(G.edges())
print(G)

g = ig.Graph.from_networkx(G)

label_list = []
for i in range(n):
    label_list.append(string.ascii_uppercase[i])

g.vs['label'] = label_list

fig, ax = plt.subplots()
ig.plot(g, target=ax)
plt.show()
"""
nx.draw(G,
        pos=nx.spring_layout(G),
        node_color="red",
        node_size=1000,
        with_labels=True)
plt.show()
plt.clf()

Update_graph(G, nodes, edges)
nx.draw(G,
        pos=nx.circular_layout(G),
        node_color="red",
        node_size=1000,
        with_labels=True)
plt.show()
plt.clf()

Update_graph(G, nodes, edges)
nx.draw_random(G,
        node_color="red",
        node_size=1000,
        with_labels=True)
plt.show()
plt.clf()
"""