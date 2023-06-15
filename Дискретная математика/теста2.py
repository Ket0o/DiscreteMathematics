import matplotlib

import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def dfs_paths(graph, start, goal):
    count = 0;
    stack = [(start, [start])]  # (vertex, path)
    print(stack)
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def Print_graph(graph):
    nx.draw_random(graph,
                     node_color='red',
                     node_size=1000,
                     with_labels=True, )
    plt.show()

G = nx.Graph()

print("Введите n:")
n = int(input())

nodes = []
edges = []
stroka = ""

for i in range(1, n + 1):
    nodes.append(i)

mas = rnd.random_integers(0, 1, size=(n, n))

for i in range (n):
    stroka = stroka + str(i + 1) + " "
print("  ", stroka)

for i in range (n):
    print(i+1, mas[i])

for i in range(0, n):
    for j in range(0, n):
        if (mas[i, j] == 0):
            continue
        if (mas[i, j] == 1):
            edges.append((i + 1, j + 1))

G.add_nodes_from(nodes)
G.add_edges_from(edges)

print()
print(G.nodes())
print(G.edges())
print(G)

print(list(dfs_paths(G, 1, n)))

Print_graph(G)
plt.clf()