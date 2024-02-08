import mysql.connector
import csv
from dbConnection import getDbConnection

# Connect to DB
mydb = getDbConnection()

cursor = mydb.cursor()

# Function to import all classrooms into DB
def importClassrooms(csvFileName):
    with open(csvFileName, "r") as csvFile:
        reader = csv.reader(csvFile, delimiter="\n")
        for row in reader:
            try:
                room = row[0].split(" ")
                building = room[0].strip()
                number = room[1]
                query = "INSERT INTO classrooms (building, room, problemsAll, problemsMonth, problemsWeek) VALUES (%s, %s, 0, 0, 0)"
                val = (building, number)
                cursor.execute(query, val)
                mydb.commit()
            except mysql.connector.Error as e:
                print(e)

fileName = "Classrooms.csv"
importClassrooms(fileName)
mydb.close()
print("Done.")
