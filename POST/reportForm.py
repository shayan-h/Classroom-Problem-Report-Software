import mysql.connector
import configparser as cp

config = cp.ConfigParser()
config.read('config.ini')

db_host = config['Database']['host']
db_user = config['Database']['username']
db_db = config['Database']['database']
db_password = config['Database']['password']

problems_array = ["Laptop VGA Video", "Laptop VGA Audio", "Laptop HDMI Video", "Laptop HDMI Audio", "Desktop Video", "Desktop Audio", "Speaker Issue",
                "Data Projector", "Blue-ray Controls", "Document Camera", "Podium Microphone", "AppleTV", "Control System", "Missing Equipment", 
                "Wireless Microphone", "Other"]

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

def createProblemReport(classroomId, problemType, problemDes):
    try: 
        query = "INSERT INTO reports (classroomId, problemType, problemDes, resolved, reportedBy) VALUES (%s, %s, %s, 1, 'Student')"
        val = (classroomId, problemType, problemDes)
        cursor.execute(query, val)
        mydb.commit()
        return True
    except mysql.connector.Error as e:
        print(e)
        return False



print("======PROBLEM REPORT FORM=======")
keepLooping = True
while keepLooping:
    building = input("Enter building ID: ")
    room = input("Enter room number: ")
    roomExists, classroomId = checkIfRoomExists(building, room)
    if (not roomExists):
        print("Room does not exist")
        break
    i = 1
    for problem in problems_array:
        print(str(i) + ". " + problem)
        i += 1
    problemNum = input("Enter problem digit: (ex. \"1\" for Laptop VGA Video) ")
    problemDes = input("Enter a short description of the problem: ")
    if (createProblemReport(classroomId, problems_array[int(problemNum) - 1], problemDes)):
        print("Problem report succesfully made.")
    else:
        print("Problem report failed.")
    cont = input("Do you want to make another problem report? (y or n) ")
    if (cont == 'n'):
        keepLooping = False