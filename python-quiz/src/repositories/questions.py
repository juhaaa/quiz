import random
from connection import get_db_connection


class Questions:
    
    #Class get connection to question database

    def __init__(self, connection):
        self.amount = 0
        self._db = connection
        self._cur = self._db.cursor()
        
        
    #Returns specific amount of tuples, after randomizing the order. Tuples contain target country, correct and false answers.
    #DB under progress.

    def get_questions(self):
        
        data = self._cur.execute("SELECT * FROM Countries ORDER BY RANDOM() LIMIT 1").fetchall()
        return data

