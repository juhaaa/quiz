import os
from os.path import exists
import csv


#get path

dir = os.path.dirname(__file__)  # pylint: disable=redefined-builtin
path = os.path.join(dir, "..", "..", "data", "highscores.csv")

#check file existing
#if not, create

def file_check():
    if not exists(path):
        file = open(path, "w")
        file.close()

# saves highscore to a .csv file ordered by score

def save_to_file(highscore):
    if highscore.score == 0:
        return
    scores = []
    file_check()
    if check_scores(highscore.score):
        highscore.name = get_player_name()
        score = [highscore.name, highscore.score, highscore.date]
        scores.append(score)
        
        with open(path, "r") as file:
            for row in file:
                scores.append(row.strip().split(","))
        scores = scores[:10]
        scores.sort(key= lambda x: int(x[1]), reverse= True)
        
        with open(path, "w", encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            for row in scores:
                writer.writerow(row)


# checks does the current score qualify for top list

def check_scores(score):
    data = read_data()
    if data[0] == 10:
        if data[1] >= score:
            return False
        else:
            return True
    else:
        return True

# prints saved highscores top-10

def print_scores():
    file_check()
    with open(path, "r") as file:
            for row in file:
                score = (row.strip().split(","))
                print(
                f"Player: {score[0]}, Score: {score[1]}, Date: {score[2]}"
                )
    

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

# if user makes it to the list,
# we need a name

def get_player_name():
    while True:
        player_name = input("Write your name here: ")
        if len(player_name) < 20:
            break
        print("20 characters max!")
    return player_name

            


if __name__ == "__main__":
    pass