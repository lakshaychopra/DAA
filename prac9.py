from collections import defaultdict
import mysql.connector
import networkx as nx
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, vertices):
        self. v = vertices
        self. ListVertices = []

    def AddEdge(self,rows):

        for row in rows:
            rm1 = [row[0], row[1], row[2]]
            self.ListVertices.append(rm1)
        return(self.ListVertices)

    def printArr(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.v):
            print("% d \t\t % d" % (i, dist[i]))

    def BellmanAndFord(self, src):

        dist = [float('inf')] * self.v

        dist[src] = 0
        s = []
        for i in range(0,self.v-1):

            for u,v,w in self.ListVertices:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    s.append([u,v,dist[v]])
        for u, v, w in self.ListVertices:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("Graph Contain a Negative Cycle")
        return s
        #self.printArr(dist)

g = Graph(5)
sql = "select * from bellmanford"
con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="college")
cursor = con.cursor()
cursor.execute(sql)
rows = cursor.fetchall()
table = g.AddEdge(rows)


df1 = pd.DataFrame(table, columns = ['Source Node', 'Destination Node','Weight'])
print("Before Applying Bellman and Ford Algorithm :")
print(df1)


plt.figure(figsize=(8,5))
edgeLables={}
for i in range(0,len(table)):
    key=(table[i][0],table[i][1])
    value=table[i][2]
    edgeLables[key]=value


spanningTree = nx.from_pandas_edgelist(df1, source='Source Node', target='Destination Node', edge_attr=True)
pos = nx.circular_layout(spanningTree)
nx.draw(spanningTree,pos,with_labels=True)
nx.draw_networkx_edge_labels(spanningTree,pos,edge_labels=edgeLables)

plt.show()

d = g.BellmanAndFord(0)

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
pos = nx.circular_layout(Dgraph)
nx.draw(Dgraph,pos,with_labels=True)
nx.draw_networkx_edge_labels(Dgraph,pos,edge_labels=minLables)
plt.show()
