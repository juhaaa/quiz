import random


class Questions:

    # Class get connection to question database
    def __init__(self, connection):
        self._db = connection

    # Returns tuple of correct answer, country name and list of answers,
    # after randomizing the order.
    # Tuples contain target country, correct and false answers.
    # DB under progress.
    def get_questions(self):

        data = self._db.execute(
            "SELECT * FROM Countries ORDER BY RANDOM() LIMIT 1").fetchall()
        cca2 = data[0][0]
        cname = data[0][1]
        correct = data[0][2]
        if correct == "":
            correct = "No capital city"
        answers = self.get_wrong_answers(cca2)
        answers.append(correct)
        random.shuffle(answers)
        return correct, cname, answers

    # Gets answers for question. Answers usually cities within the same country.
    # If not possible, gathers answers from other countries.

    def get_wrong_answers(self, cca2):

        data = self._db.execute(
            "SELECT Cities.name FROM Cities, Countries WHERE Cities.cca2=? AND Cities.cca2=Countries.cca2 AND Countries.capital<>Cities.name ORDER BY RANDOM() LIMIT 3", # pylint: disable=line-too-long
            [cca2]).fetchall()
        answer_count = len(data)

        if answer_count < 3:
            amount = 3 - answer_count
            extra_answers = self._db.execute(
                "SELECT Cities.name FROM Cities, Countries WHERE Countries.cca2=Cities.cca2 AND Countries.capital<>Cities.name ORDER BY RANDOM() LIMIT ?", # pylint: disable=line-too-long
                [amount]).fetchall()
            for i in extra_answers:
                data.append(i)

        return [data[0][0], data[1][0], data[2][0]]
