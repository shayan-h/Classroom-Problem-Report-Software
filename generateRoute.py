import mysql.connector
from IPython.display import display
from dbConnection import getDbConnection
import pandas as pd

mydb = getDbConnection()

cursor = mydb.cursor()

def printProblemList():
    query = "SELECT classrooms.building, classrooms.room, reports.problemType, reports.problemDes, reports.reportTime FROM reports INNER JOIN classrooms ON reports.classroomID=classrooms.id ORDER BY reports.problemTypeID ASC"
    cursor.execute(query, None)
    # result = cursor.fetchall()
    # df = pd.DataFrame(result, columns=['Building', 'Room', 'Problem', 'Description', 'Reported At'])
    # display(df)
    # mydb.commit()

printProblemList()

