import mysql.connector
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

def checkIfRoomExists(building, room):
    query = "SELECT * FROM classrooms WHERE building = %s AND room = %s"
    val = (building, room)
    cursor.execute(query, val)
    result = cursor.fetchall()
    mydb.commit()
    if not result:
        return False, -1
    classroomId = result[0][0]
    return True, classroomId


print("======PROBLEM REPORT FORM=======")
while True:
    building = input("Enter building ID: ")
    room = input("Enter room number: ")
    roomExists, classroomId = checkIfRoomExists(building, room)
    if (not roomExists):
        print("Room does not exist")
        break
    print(classroomId)
