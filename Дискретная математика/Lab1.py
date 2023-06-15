import graphviz as gv
import string
import matplotlib
import numpy
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
import random
matplotlib.use('TkAgg')


def CreateGraph(edges, nodes):
    G = gv.Graph(format='png')

    for node in nodes:
        G.node(node, node)

    G.edges(edges)

    G.view()

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

new_nodes = [nodes]
temporaryNodes = random.shuffle(nodes)
for i in range(n - 1):
    while(len(new_nodes) != 4):
        for j in range(len(new_nodes)):
            if(temporaryNodes not in new_nodes):
                new_nodes.append(temporaryNodes)
            else:
                temporaryNodes = random.shuffle(nodes)
    break

for i in range(n):
    CreateGraph(edges, new_nodes[i])

"""
сумма всех степеней вершин не больше n/2
(\/)симметрия
(\/)псевдограф (кратные ребра и петли)
"""