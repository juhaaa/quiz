import sqlite3
import random

class Questions:
    
    #Class connects to question database

    def __init__(self):
        self.amount = 0
        self.db = sqlite3.connect("data/data.db")
        
    #Returns specific amount of tuples, after randomizing the order. Tuples contain target country, correct and false answers.
    #DB under progress.

    def get_questions(self, amount):
        self.amount = amount
        data = self.db.execute("SELECT Name, Correct, c1, c2, c3 FROM Countries;").fetchall()
        random.shuffle(data)
        return data[:self.amount]

a = Questions()
print(a.get_questions(2))