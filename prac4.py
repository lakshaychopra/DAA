import mysql.connector
import numpy as np
#Creating printing function for all the Three Criterias
def display(result,criteria):
    i = 0
    print(criteria)
    print("===================")
    print("Item \t Weight")
    for selectedItem in result[0]:
        print(result[2][i], "\t", selectedItem)
        i += 1
    print("Total Value:", result[1])
    print("Total Weight:", sum(result[0]))
    print("===================")

# Function to solve with criteria-1
def knapsack_c1(itemWeight,itemValue):
    weightsTaken_c1 = []
    itemTaken_c1 = []
    valueTaken_c1 = 0
    itemValueSorted = sorted(itemValue,reverse=True)

    for item in itemValueSorted:
        selectValue_c1 = itemValue.index(item)
        weightsTaken_c1.append(itemWeight[selectValue_c1])
        itemTaken_c1.append(itemName[selectValue_c1])
        valueTaken_c1 = valueTaken_c1 + item
        if sum(weightsTaken_c1) > maxWeight:
            weightsTaken_c1.remove(itemWeight[selectValue_c1])
            itemTaken_c1.remove(itemName[selectValue_c1])
            valueTaken_c1 = valueTaken_c1 - item
        elif sum(weightsTaken_c1) == maxWeight:
            return weightsTaken_c1, valueTaken_c1, itemTaken_c1

    return weightsTaken_c1,valueTaken_c1,itemTaken_c1

# Function to solve with criteria-2
def knapsack_c2(itemWeight,itemValue):
    weightsTaken_c2 = []
    itemTaken_c2 = []
    valueTaken_c2 = 0
    itemWeightSorted = sorted(itemWeight)

    for item in itemWeightSorted:
        selectValue_c2 = itemWeight.index(item)
        weightsTaken_c2.append(item)
        itemTaken_c2.append(itemName[selectValue_c2])
        valueTaken_c2 = valueTaken_c2 + itemValue[selectValue_c2]
        if sum(weightsTaken_c2) > maxWeight:
            weightsTaken_c2.remove(item)
            itemTaken_c2.remove(itemName[selectValue_c2])
            valueTaken_c2 = valueTaken_c2 - itemValue[selectValue_c2]
        elif sum(weightsTaken_c2) == maxWeight:
            weightsTaken_c2, valueTaken_c2, itemTaken_c2

    return weightsTaken_c2,valueTaken_c2,itemTaken_c2


# Function to solve with criteria-3
def knapsack_c3(itemWeight,itemValue,valueToWeightRatio):
    weightsTaken_c3 = []
    valueTaken_c3 = 0
    itemTaken_c3 = []
    remainingWeight = 0
    for i in range(0,len(valueToWeightRatio)):
        selectValue_c3 = valueToWeightRatio.index(max(valueToWeightRatio))
        weightsTaken_c3.append(itemWeight[selectValue_c3])
        valueTaken_c3 = valueTaken_c3 + itemValue[selectValue_c3]
        itemTaken_c3.append(itemName[selectValue_c3])

        if sum(weightsTaken_c3) > maxWeight:
            weightsTaken_c3.remove(itemWeight[selectValue_c3])
            remainingWeight = maxWeight - sum(weightsTaken_c3)
            valueTaken_c3 = valueTaken_c3 - itemValue[selectValue_c3]
            weightsTaken_c3.append(remainingWeight)
            valueTaken_c3 = valueTaken_c3 + valueToWeightRatio[selectValue_c3] * remainingWeight
            return weightsTaken_c3,valueTaken_c3,itemTaken_c3
        valueToWeightRatio[selectValue_c3] = 0
    return weightsTaken_c3, valueTaken_c3, itemTaken_c3

print("Lakshay Chopra")
print("D3 CSE A2")
print("1706462")
print("===================")

# Creating the Connection With the database
con = mysql.connector.connect(user = "root", password = "",host = "127.0.0.1" ,database= "daa")
cursor = con.cursor()

#Fetching Weights and putting it in a list itemWeights
cursor.execute("select Weight from data")
weights = cursor.fetchall()
itemWeight = []
for weight in weights:
    itemWeight.append(weight[0])

#Fetching Values and putting it in a list itemValues
cursor.execute("select value from data")
values = cursor.fetchall()
itemValue = []
for value in values:
    itemValue.append(value[0])

#Fetching item name and putting it in a list itemName
cursor.execute("select item from data")
names = cursor.fetchall()
itemName = []
for name in names:
    itemName.append(name[0])

"""
itemWeight = np.array(itemWeight)
itemValue = np.array(itemValue)
"""


#Calculating value to weight ratio and puuting it in list ' valueToWeightRatio'
valueToWeightRatio= list(map(lambda x, y: x/y, itemValue, itemWeight))    # can be done with numpy array

#Setting up the Constraint: Maximum Weight that can be Taken
maxWeight = 60

result_c1 = knapsack_c1(itemWeight,itemValue)
display(result_c1,"Knapsack Criteria 1")

result_c2 = knapsack_c2(itemWeight,itemValue)
display(result_c2,"Knapsack Criteria 2")

result_c3 = knapsack_c3(itemWeight,itemValue,valueToWeightRatio)
display(result_c3,"Knapsack Criteria 3")