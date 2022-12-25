import random
from services.question_services import question_service
from services.question_services import additional_answers
from services.question_services import more_additional_answers

class Questions:
    """Class which is responsible for questions during game.
    """

    def __init__(self, connection):
        """Class gets connection to question database

        Args:
            connection (Connection): sqlite connnection object
        """
        self._db = connection


    def get_questions(self):
        """Returns tuple of correct answer, country name and list of answers,
            after randomizing the order.
            Tuples contain target country, correct and false answers.

        Returns:
            Tuple: question with correct answer and false answers
        """

        data = question_service(self._db)
        cca2 = data[0][0]
        cname = data[0][1]
        correct = data[0][2]
        if correct == "":
            correct = "No capital city"
        answers = self.get_wrong_answers(cca2)
        answers.append(correct)
        random.shuffle(answers)
        return correct, cname, answers



    def get_wrong_answers(self, cca2):
        """Gets answers for question. Answers usually cities within the same country.
            If not possible, gathers answers from other countries.

        Args:
            cca2 (str): Country code

        Returns:
            list: list with wrong answers
        """
        data = additional_answers(cca2, self._db)
        answer_count = len(data)

        if answer_count < 3:
            amount = 3 - answer_count
            extra_answers = more_additional_answers(amount, self._db)
            for i in extra_answers:
                data.append(i)

        return [data[0][0], data[1][0], data[2][0]]
