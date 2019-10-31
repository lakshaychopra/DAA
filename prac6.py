import mysql.connector
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self,vertices):
        self.V= vertices
        self.graph = []

    def addEdge(self,edge):
        self.graph.append(edge)

    def find(self, parent, i):
        if parent[i-1] == i:
            return i
        return self.find(parent, parent[i-1])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot-1] < rank[yroot-1]:
            parent[xroot-1] = yroot
        elif rank[xroot-1] > rank[yroot-1]:
            parent[yroot-1] = xroot
        else :
            parent[yroot-1] = xroot
            rank[xroot-1] += 1
    def KruskalMST(self):
        self.result =[]
        i = 0
        e = 0
        self.graph =  sorted(self.graph,key=lambda item: item[2])
        print("sorted graph is\n",self.graph)
        parent = []
        rank = []
        for node in range(1,self.V+1):
            parent.append(node)
            rank.append(0)
        while e < self.V:
            u,v,w =  self.graph[e]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
            e = e + 1
            if x != y:
                self.result.append([u,v,w])
                self.union(parent, rank, x, y)
        return self.result

def fetchAllVertices():
    sql = "select * from prims"
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="college")
    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    list = []
    for row in rows:
        rm1 = [row[0], row[1], row[2]]
        list.append(rm1)
    return list

print("Lakshay Chopra")
print("Roll No: 1706462")
table=fetchAllVertices()

df1 = pd.DataFrame(table, columns = ['Source Node', 'Destination Node','Weight'])
print("Before Applying Kruskals Algorithm :")
print(df1)
edgeLables={}

for i in range(0,len(table)):
    key=(table[i][0],table[i][1])
    value=table[i][2]
    edgeLables[key]=value

spanningTree = nx.from_pandas_edgelist(df1, source='Source Node', target='Destination Node', edge_attr=True)
plt.figure(figsize=(8,5))
pos = nx.circular_layout(spanningTree)
nx.draw(spanningTree,pos,with_labels=True)
nx.draw_networkx_edge_labels(spanningTree,pos,edge_labels=edgeLables)
plt.show()

g = Graph(5)
for x in table:
    g.addEdge(x)
MST=g.KruskalMST()
minLables={}
totalWeight=0

for i in range(0,len(MST)):
    key=(MST[i][0],MST[i][1])
    value=MST[i][2]
    totalWeight+=MST[i][2]
    minLables[key]=value
df2 = pd.DataFrame(MST, columns = ['Source Node', 'Destination Node','Weight'])
print("\nAfter Applying Kruskals Algorithm :")
print(df2)
print("Weight Of minnimum spanning Tree Formed is: ",totalWeight)
Primsgraph = nx.from_pandas_edgelist(df2, source='Source Node', target='Destination Node', edge_attr=True)
pos = nx.circular_layout(Primsgraph)
nx.draw(Primsgraph,pos,with_labels=True)
nx.draw_networkx_edge_labels(Primsgraph,pos,edge_labels=minLables)
plt.show()
