import mysql.connector
from time import *

# binSearch function is a recursive function to search The roll numbers
def binSearch(rollNumbersSorted,beg,end,requiredRollNumber ):
    while beg <= end:
        mid = (beg + end) // 2
        if rollNumbersSorted[mid] < requiredRollNumber :
            beg = mid + 1
            binSearch(rollNumbersSorted,beg,end,requiredRollNumber )
        elif rollNumbersSorted[mid] > requiredRollNumber :
            end = mid - 1
            binSearch(rollNumbersSorted, beg, end,requiredRollNumber )
        elif rollNumbersSorted[mid] == requiredRollNumber :
            return mid
    return -1

print("Lakshay Chopra")
print("D3 CSE A2")
print("1706462")


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


# Sorting the List of roll Numbers

rollNumbersSorted = rollNumbers.copy()
rollNumbersSorted.sort()
beg = 0
end = len(rollNumbersSorted) - 1

# Getting The Roll number from the user

requiredRollNumber = int(input("\nEnter The Roll Number To Be Searched"))

# Calling the binSearch Function to search the roll number
timestamp1 = time()

result = binSearch(rollNumbersSorted,beg,end,requiredRollNumber)

timestamp2 = time()

if result == -1:
    print("=================")
    print("Roll Number Not Found")
    print("=================")
else:
    place = rollNumbers.index(rollNumbersSorted[result])
    print("=================")
    print("Roll Number Found")
    print("=================")
    print("S.No. \t Roll Number \n {} \t {} ".format(place + 1, requiredRollNumber))

print("=================")
print("Required Time for the Search:",timestamp2 - timestamp1)
print("=================")