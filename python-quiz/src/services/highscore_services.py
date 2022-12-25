import os
from os.path import exists
import csv


#get path

dir = os.path.dirname(__file__)  # pylint: disable=redefined-builtin
path = os.path.join(dir, "..", "..", "data", "highscores.csv")



def file_check():
    """Checks if file exists. If not, create and confirm.

    Returns:
        Boolean: Confirmation
    """
    if not exists(path):
        with open(path, "w", encoding='UTF8') as file:
            file.close()
    return True


def save_to_file(highscore):
    """saves highscore to a .csv file ordered by score.

    Args:
        highscore (Higschore): Higscore object consists of information about game finished.

    """
    if highscore.score == 0:
        return
    scores = []
    score = [highscore.name, highscore.score, highscore.date]
    scores.append(score)

    with open(path, "r", encoding='UTF8') as file:
        for row in file:
            scores.append(row.strip().split(","))
    scores = scores[:10]
    scores.sort(key= lambda x: int(x[1]), reverse= True)

    with open(path, "w", encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        for row in scores:
            writer.writerow(row)


def check_scores(score):
    """Checks does the current score qualify for top list by evaluating .csv's
    lowest score and score.

    Args:
        score (int): score to evaluate

    Returns:
        boolean: outcome depends of the evaluation. True if score makes it to the list.
    """
    data = read_data()
    if data[0] == 10:
        if data[1] >= score:
            return False
    return True



def get_scores():
    """ Reads the store .csv file.
    Returns saved highscores top-10 as str list to be printed for user.

    Returns:
        list: list of highscores as str.
    """
    scores_as_str_list = []
    file_check()

    with open(path, "r", encoding='UTF8') as file:
        i = 1
        for row in file:
            score = (row.strip().split(","))
            scores_as_str_list.append(
                f"{i}. {score[0]}, Score: {score[1]}, Date: {score[2]}"
                )
            i += 1
    return scores_as_str_list




def read_data():
    """Reads highscores.csv and returns amount of scores saved
    and minimum score.

    Returns:
        Tuple: score amount in int and min_score int
    """
    min_score = 1000
    file_check()
    with open(path, "r", encoding='UTF8') as file:
        score_amount = len(file.readlines())
    with open(path, "r", encoding='UTF8') as file:
        for row in file:
            rows = row[:-1].split(",")
            if int(rows[1]) < min_score:
                min_score = int(rows[1])
    return score_amount, min_score
    