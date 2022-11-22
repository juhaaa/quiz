import sqlite3
import random
from connection import get_db_connection


class Questions:
    
    #Class connects to question database

    def __init__(self, connection):
        self.amount = 0
        self._db = connection
        
    #Returns specific amount of tuples, after randomizing the order. Tuples contain target country, correct and false answers.
    #DB under progress.

    def get_questions(self, amount):
        self.amount = amount
        data = self._db.execute("SELECT Name, Correct, c1, c2, c3 FROM Countries;").fetchall()
        random.shuffle(data)
        return data[:self.amount]

a = Questions(get_db_connection())
print(a.get_questions(2))