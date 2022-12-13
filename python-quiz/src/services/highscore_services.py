import os
from os.path import exists
import csv
from ui.highscore_ui import user_input_ui


#get path

dir = os.path.dirname(__file__)  # pylint: disable=redefined-builtin
path = os.path.join(dir, "..", "..", "data", "highscores.csv")

#check file existing
#if not, create

def file_check():
    if not exists(path):
        with open(path, "w", encoding='UTF8') as file:
            file.close()
    return True

# saves highscore to a .csv file ordered by score

def save_to_file(highscore, stdscr):
    if highscore.score == 0:
        return False
    scores = []
    file_check()
    if check_scores(highscore.score):
        highscore.name = user_input_ui(stdscr)
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
            return True

# checks does the current score qualify for top list

def check_scores(score):
    data = read_data()
    if data[0] == 10:
        if data[1] >= score:
            return False
    return True

# return saved highscores top-10

def get_scores():
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


# reads highscores.csv and returns amount of scores saved
# and minimum score.

def read_data():
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
