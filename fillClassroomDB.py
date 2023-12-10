import mysql.connector
import csv
import configparser as cp 

config = cp.ConfigParser()
config.read('config.ini')

db_host = config['Database']['host']
db_user = config['Database']['username']
db_db = config['Database']['database']
db_password = config['Database']['password']


# Connect to DB
mydb = mysql.connector.connect(
    host = db_host,
    user = db_user,
    database = db_db,
    password = db_password
)

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
print("Done.")