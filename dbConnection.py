import mysql.connector
import configparser as cp

config = cp.ConfigParser()
config.read('config.ini')

db_host = config['Database']['host']
db_user = config['Database']['username']
db_db = config['Database']['database']
db_password = config['Database']['password']

def getDbConnection():
    mydb = mysql.connector.connect(
        host = db_host,
        user = db_user,
        database = db_db,
        password = db_password
    )
    return mydb

