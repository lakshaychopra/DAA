import mysql.connector as sql
from collections import defaultdict
import networkx as nx
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
print("Malika Jain \nD3CSEA2 1706465")

conn = sql.connect(host='127.0.0.1', user='root', password='', database='daa')

cur = conn.cursor()

cur.execute('select * from tsp')
data = list(cur)

g1 = defaultdict(list)
df1 = pd.DataFrame(data, columns = ['Source Node', 'Destination Node','Weight'])
print(df1)
lables={}
for i in range(len(data)):
    key=(data[i][0],data[i][1])
    lables[key]=data[i][2]
Dgraph = nx.from_pandas_edgelist(df1, source='Source Node', target='Destination Node', edge_attr=True)
pos = nx.circular_layout(Dgraph)
nx.draw(Dgraph, pos, with_labels=True)
nx.draw_networkx_edge_labels(Dgraph, pos, edge_labels=lables)
plt.show()
for i, j, k in data:
    g1[i] += [[j, k]]

def tsp(graph):
    not_visited = set(graph.keys())
    starting = 'office'
    not_visited.remove(starting)
    costList=[]
    current = starting
    cost = 0
    nodes = [starting]
    minimum = sorted(graph[current], key=lambda x: x[1])

    while not_visited:
        current = minimum[0][0]
        if current in not_visited:
            cost += minimum[0][1]
            not_visited.remove(current)
            costList.append(minimum[0][1])

            minimum = sorted(graph[current], key=lambda x: x[1])

            nodes.append(current)

        else:
            minimum.pop(0)
    for i in graph[current]:
        if i[0] == starting:
            costList.append(i[1])
            cost += i[1]
            nodes.append(i[0])
    print('Minimum Cost:', cost)
    print('Visiting Sequence:', nodes)
    print("cost List Is ",costList)
    list=[]
    minLables={}
    for i in range(0,6):
        innerList=[]
        innerList.append(nodes[i])
        innerList.append(nodes[i+1])
        innerList.append(costList[i])
        list.append(innerList)
        key = (innerList[0],innerList[1])
        minLables[key] = costList[i]
    print(list)
    df2 = pd.DataFrame(list, columns=['Source Node', 'Destination Node', 'Weight'])
    print(df2)
    Dgraph = nx.from_pandas_edgelist(df2, source='Source Node', target='Destination Node', edge_attr=True)
    pos = nx.circular_layout(Dgraph)
    nx.draw(Dgraph, pos, with_labels=True)
    nx.draw_networkx_edge_labels(Dgraph, pos, edge_labels=minLables)
    plt.show()
tsp(g1)
