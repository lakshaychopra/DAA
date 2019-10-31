import mysql.connector
from time import *

def mergeSort(rollNumbers):
    if len(rollNumbers) > 1:
        mid = len(rollNumbers) // 2  # Finding the mid of the array
        Left = rollNumbers[:mid]  # Dividing the array elements
        Right = rollNumbers[mid:]  # into 2 halves
        mergeSort(Left)  # Sorting the first half
        mergeSort(Right)  # Sorting the second half


        i = j = k = 0

        # Copy data to temp arrays Left[] and Right[]
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                rollNumbers[k] = Left[i]
                i += 1
            else:
                rollNumbers[k] = Right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(Left):
            rollNumbers[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            rollNumbers[k] = Right[j]
            j += 1
            k += 1

print("Lakshay Chopra")
print("D3 CSE A2")
print("1706462")
print("=================")
# Creating the Connection With the database

sql = "select Roll_Numbers from University_Roll_Numbers"
con = mysql.connector.connect(user = "root", password = "",host = "127.0.0.1" ,database= "Student_Details")
cursor = con.cursor()
cursor.execute(sql)

# Creating a list of roll numbers fetched from the table 'University_Roll_Numbers' of database 'Student_Details'
rollNumbers = []
rows = cursor.fetchall()
for row in rows:
    rollNumbers.append(row[0])

print("Unsorted Roll Numbers")
print(rollNumbers)
print("=================")

timestamp1 = time()
mergeSort(rollNumbers)
timestamp2 = time()


print("Sorted Roll Numbers")
print(rollNumbers)
print("=================")
print("Time Required For Sorting:",timestamp2 - timestamp1)
print("=================")