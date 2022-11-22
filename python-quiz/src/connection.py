import sqlite3

#Connects to SQL database

def get_db_connection():
    dbconnection = sqlite3.connect("data/data.db")
    return dbconnection

