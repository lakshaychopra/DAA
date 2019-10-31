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

def minDistance(dist, sptSet):

        # Initilaize minimum distance for next node
    min = float('inf')
    V = 5
        # Search not nearest vertex not in the
        # shortest path tree
    for v in range(V):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index

def dijkstra(vertices,src,graph):

    dist = [float('inf')] * vertices
    dist[src] = 0
    sptSet = [False] * vertices
    V = 5
    s = []
    t = []

    for cout in range(vertices):
        u = minDistance(dist, sptSet)
        sptSet[u] = True

        for v in range(vertices):
            if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                s.append([u,v,dist[v]])


    return s

def fetchAllVertices():
    sql = "select * from dijikstra"
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="college")
    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    list = []
    for row in rows:
        rm1 = [row[0],row[1],row[2]]
        list.append(rm1)
    return list
print("Lakshay Chopra")
print("1706462")
print("CSE A2")
G = fetchAllVertices()

df1 = pd.DataFrame(G, columns = ['Source Node', 'Destination Node','Weight'])
print("Before Applying Dijikstra's  Algorithm :")
print(df1)

edgeLables={}

for i in range(0,len(G)):
    key=(G[i][0],G[i][1])
    value=G[i][2]
    edgeLables[key]=value
#print("edge", edgeLables)
SP = nx.from_pandas_edgelist(df1, source='Source Node', target='Destination Node', edge_attr=True)
plt.figure(figsize=(8,5))
pos = nx.layout.planar_layout(SP)
#nx.draw(SP)
nx.draw(SP,pos,with_labels=True)
nx.draw_networkx_edge_labels(SP,pos,edge_labels=edgeLables)
plt.show()

a = createAdjMatrix(5,G)
d = dijkstra(5,3,a)
#print(d)

minLables={}
totalWeight=0
for i in range(0,len(d)):
    key=(d[i][0],d[i][1])
    value=d[i][2]
    #print(value)
    totalWeight+=d[i][2]
    minLables[key] = value

#print(minLables)
df2 = pd.DataFrame(d, columns = ['Source Node', 'Destination Node','Weight'])
print("\nAfter Applying dijikstra Algorithm :")
print(df2)
print("Total Weight : ",totalWeight)
Dgraph = nx.from_pandas_edgelist(df2, source='Source Node', target='Destination Node', edge_attr=True)
pos = nx.planar_layout(Dgraph)
nx.draw(Dgraph,pos,with_labels=True)
nx.draw_networkx_edge_labels(Dgraph,pos,edge_labels=minLables)
plt.show()
#print(d)


#print(a)
