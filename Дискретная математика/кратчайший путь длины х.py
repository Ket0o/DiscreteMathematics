import igraph as ig
import matplotlib.pyplot as plt
import numpy.random as rnd
import string
import numpy as np

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


def FindShortestPath(size: int, start: int, end: int, matrix1):
    dictionary = {}
    temp = []
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix1)):
            if matrix1[i, j] == 1:
                temp.append(j + 1)
        dictionary[i + 1] = temp
        temp = []
    print(dictionary)

    explored = []
    queue = [[start]]

    if start == end:
        print("Выбран один и тот же узел")
        return

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            continue

        if node not in explored:
            neighbours = dictionary[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == end and len(new_path) - 1 == size:
                    print(f"Кратчайший путь длины {size} = ", *new_path)
                    print(len(new_path))
                    return
            explored.append(node)
    print(f"Нет пути длины {size}")


"""
def CreateGraph(edges, nodes):
    G = ig.Graph(n=n, edges=edges)
    G.vs['label'] = nodes
    return G
"""

def PrintGraph(G, color):
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 5)
    ig.plot(G, layout=G.layout("random"), target=ax, vertex_color=color)


print("Введите n:")
n = int(input())

nodes = [i + 1 for i in range(n)]
edges = []
matrixtest = np.zeros((n, n), dtype=int)

# заполнение матрицы
for i in range(0, n):
    for j in range(0 + i, n):
        matrixtest[i, j] = rnd.randint(2)
        if j == i:
            matrixtest[i, j] = 1

matrix2 = np.transpose(matrixtest).copy()

for i in range(n):
    matrix2[i, i] = 0

matrixtest = matrix2 + matrixtest

for i in range(0, len(matrixtest)):
    for j in range(0, len(matrixtest)):
        if matrixtest[i, j] == 1:
            edges.append((str(i + 1), str(j + 1)))

# stroka = ""
# vector = rnd.random_integers(0, 2, size=(n, n))
#
# for i in range(0, n):
#     nodes.append(string.ascii_uppercase[i])
#
# mas = numpy.tril(vector) + numpy.tril(vector, -1).T
#
# for i in range (n):
#     stroka = stroka + string.ascii_uppercase[i] + " "
# print("  ", stroka)
#
# for i in range (n):
#     print(string.ascii_uppercase[i], mas[i])

# for i in range(0, n):
#     for j in range(i, n):
#         if (mas[i, j] == 0):
#             continue
#         if (mas[i, j] == 1):
#             edges.append((i , j))
#         if (mas[i, j] == 2):
#             edges.append((i, j))
#             edges.append((j, i))
#
colorsForNodes = []

for i in range(n):
    for v in range(n):
        colorsNodes[v] = GetColorForNode(v, CreateGraph(edges, nodes))
        colorsForNodes.append(GetColorForNode(v, CreateGraph(edges, nodes)))
    PrintGraph(CreateGraph(edges, nodes), colorsForNodes)

plt.show()
print(nodes)
print(edges)

print("Введите вершину - начало:")
i = int(input())
print("Введите вершину - конец:")
j = int(input())

while (True):
    l = int(input("Введите длину пути: "))
    FindShortestPath(l, 1, 3, matrixtest)