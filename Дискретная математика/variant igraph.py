import igraph as ig
import matplotlib.pyplot as plt
import numpy.random as rnd
import string
import numpy

colorsNodes = {}

def Coloring(node, color, G):
    for neighbor in G.neighbors(node):
        if neighbor == node:
            continue
        colorNeighbor = colorsNodes.get(neighbor, None)
        if colorNeighbor == color:
            return False
    return True

colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black', 'Pink', 'Orange', 'White', 'Gray', 'Purple', 'Brown', 'Navy']

def GetColorForNode(node, G):
    for color in colors:
        if Coloring(node, color, G):
            return color

def CreateGraph(edges, nodes):
    G = ig.Graph(n=n, edges=edges)
    G.vs['name'] = nodes
    G.vs['label'] = nodes
    return G

def PrintGraph(G, color):
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 5)
    ig.plot(G, layout=G.layout("random"), target=ax, vertex_color=color)

print("Введите n:")
n = int(input())

path = []
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
            edges.append((i , j))
        if (mas[i, j] == 2):
            edges.append((i, j))
            edges.append((j, i))

colorsForNodes = []

for i in range(n):
    for v in range(n):
        colorsNodes[v] = GetColorForNode(v, CreateGraph(edges, nodes))
        colorsForNodes.append(GetColorForNode(v, CreateGraph(edges, nodes)))
    PrintGraph(CreateGraph(edges, nodes), colorsForNodes)

plt.show()

G = CreateGraph(edges, nodes)

while(True):
    print("Введите вершину - начало:")
    i = input()
    print("Введите вершину - конец:")
    j = input()
    print("Введите длину пути:")
    l = int(input())

    path = G.get_all_simple_paths(i, to=j, mode="all")

    print(path, "\n")

    k = -1

    for i in range(len(path)):
        if (len(path[i]) == l + 1):
            k = i
            break


    if(k != -1):
        s = ""
        answer = path[k]
        for i in range(len(answer)):
            s = s + string.ascii_uppercase[answer[i]]
        print(s)
    else:
        print("Error")