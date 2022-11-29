from repositories.questions import Questions
from connection import get_db_connection


a = Questions(get_db_connection())
print(a.get_questions())