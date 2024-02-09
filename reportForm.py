import mysql.connector
from dbConnection import getDbConnection

problems_array = ["Laptop VGA Video", "Laptop VGA Audio", "Laptop HDMI Video", "Laptop HDMI Audio", "Desktop Video", "Desktop Audio", "Speaker Issue",
                "Data Projector", "Blue-ray Controls", "Document Camera", "Podium Microphone", "AppleTV", "Control System", "Missing Equipment", 
                "Wireless Microphone", "Other"]

# Connect to DB
mydb = getDbConnection()

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

def createProblemReport(classroomId, problemType, problemDes, problemNum):
    try: 
        query = "INSERT INTO reports (classroomId, problemType, problemDes, resolved, reportedBy, problemTypeID) VALUES (%s, %s, %s, 1, 'Student', %s)"
        val = (classroomId, problemType, problemDes, problemNum)
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
        continue
    i = 1
    for problem in problems_array:
        print(str(i) + ". " + problem)
        i += 1
    problemNum = input("Enter problem digit: (ex. \"1\" for Laptop VGA Video) ")
    problemDes = input("Enter a short description of the problem: ")
    if (createProblemReport(classroomId, problems_array[int(problemNum) - 1], problemDes, problemNum)):
        print("Problem report succesfully made.")
    else:
        print("Problem report failed.")
    cont = input("Do you want to make another problem report? (y or n) ")
    if (cont == 'n'):
        keepLooping = False
