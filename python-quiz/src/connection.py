import os
import sqlite3

#Connects to SQL database

dir = os.path.dirname(__file__)

def get_db_connection():
    dbconnection = sqlite3.connect(os.path.join(dir, "..", "data", "data.db"))
    return dbconnection

