from time import *

def quickSort(rollNumbers,beg,end):
    if(beg < end):
        part = partition(rollNumbers,beg,end)
        quickSort(rollNumbers,beg,part - 1)
        quickSort(rollNumbers,part + 1,end)

def partition(rollNumbers,beg,end):
    pivot = rollNumbers[end]
    i = beg - 1
    for j in range(beg,end):
        if rollNumbers[j] < pivot:
            i = i + 1
            rollNumbers[i],rollNumbers[j] = rollNumbers[j],rollNumbers[i]   # SWAP
    rollNumbers[i+1],rollNumbers[end] = rollNumbers[end],rollNumbers[i+1]
    return (i + 1)

print("Lakshay Chopra")
print("D3 CSE A2")
print("1706462")
print("=================")

sql = "select Roll_Numbers from University_Roll_Numbers"
con = mysql.connector.connect(user = "root", password = "",host = "127.0.0.1" ,database= "Student_Details")
cursor = con.cursor()
cursor.execute(sql)

rollNumbers = []
rows = cursor.fetchall()
for row in rows:
    rollNumbers.append(row[0])

beg = 0
end = len(rollNumbers) - 1

print("Unsorted Roll Numbers")
print(rollNumbers)
print("=================")

timestamp1 = time()

quickSort(rollNumbers,beg,end)

timestamp2 = time()


print("Sorted Roll Numbers")
print(rollNumbers)
print("=================")
print("Time Required For Sorting:",timestamp2 - timestamp1)
print("=================")