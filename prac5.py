import mysql.connector
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def createAdjMatrix(V, G):
    adjMatrix = []
    for i in range(0, V):
        adjMatrix.append([])
        for j in range(0, V):
            adjMatrix[i].append(0)
    for i in range(0, len(G)):
        adjMatrix[G[i][0]][G[i][1]] = G[i][2]
        adjMatrix[G[i][1]][G[i][0]] = G[i][2]
    return adjMatrix

def prims(V, G):
    adjMatrix = createAdjMatrix(V, G)
    vertex = 1
    MST = []
    edges = []
    visited = []
    minEdge = [None, None, float('inf')]
    while len(MST) != V - 1:
        visited.append(vertex)
        for r in range(0, V):
            if adjMatrix[vertex][r] != 0:
                edges.append([vertex, r, adjMatrix[vertex][r]])
        for e in range(0, len(edges)):
            if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
                minEdge = edges[e]
        if minEdge==  [None, None, float('inf')]:
            return MST
        edges.remove(minEdge)
        MST.append(minEdge)
        vertex = minEdge[1]
        minEdge = [None, None, float('inf')]

def fetchAllVertices():
    sql = "select * from prims"
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="college")
    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    list = []
    for row in rows:
        rm1 = [row[0],row[1],row[2]]
        list.append(rm1)
    return list

print("Lakshay")
print("1706462")
print("D3 CSE A2")

graph=fetchAllVertices()


df1 = pd.DataFrame(graph, columns = ['Source Node', 'Destination Node','Weight'])
print("Before Applying Prims Algorithm :")
print(df1)
edgeLables={}

for i in range(0,len(graph)):
    key=(graph[i][0],graph[i][1])
    value=graph[i][2]
    edgeLables[key]=value

spanningTree = nx.from_pandas_edgelist(df1, source='Source Node', target='Destination Node', edge_attr=True)
plt.figure(figsize=(8,5))
pos = nx.circular_layout(spanningTree)
nx.draw(spanningTree,pos,with_labels=True)
nx.draw_networkx_edge_labels(spanningTree,pos,edge_labels=edgeLables)
plt.show()

MST=prims(9, graph)
minLables={}
totalWeight=0
for i in range(0,len(MST)):
    key=(MST[i][0],MST[i][1])
    value=MST[i][2]
    totalWeight+=MST[i][2]
    minLables[key]=value
df2 = pd.DataFrame(MST, columns = ['Source Node', 'Destination Node','Weight'])
print("\nAfter Applying Prims Algorithm :")
print(df2)
print("Weight Of minnimum spanning Tree Formed is: ",totalWeight)
Primsgraph = nx.from_pandas_edgelist(df2, source='Source Node', target='Destination Node', edge_attr=True)
pos = nx.circular_layout(Primsgraph)
nx.draw(Primsgraph,pos,with_labels=True)
nx.draw_networkx_edge_labels(Primsgraph,pos,edge_labels=minLables)
plt.show()
