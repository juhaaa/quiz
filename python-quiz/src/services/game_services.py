from repositories.questions import Questions
from services.connection_services import get_db_connection


#init questions

def init_questions():
    question_object = Questions(get_db_connection())
    return question_object

# main game loop, returns score

def play_game(game):
    question_object = init_questions()
    game.running = True
    
    while game.running:
        question = question_object.get_questions()
        correct, country, answers = question[0], question[1], question[2]
        print_question(country, answers)
        user_input = get_input()
        if user_input == 0:
            break
        check_correct(game, correct, answers[user_input - 1])
        game.rounds += 1
        if game.rounds == 10:
            game.running = False
    
    print_score(game)
    return game.score
    

# checks answers outcome
# updates game- object accordingly

def check_correct(game, correct, answer):
    if correct == answer:
        print(f"You are correct. {correct} is the right answer!")
        game.increase_score()
        print(game.score, "\n")
    else:
        print("Wrong answer!")
        print(game.score, "\n")

# gets input from user during gameplay

def get_input():
    valid = [0, 1, 2, 3, 4]
    while True:
        user_input = input("Choose between 1-4, zero ends: ")
        try:
            user_input = int(user_input)
        except ValueError:
            print("Input not valid, try again")
            continue
        if user_input in valid:
            break
        print("Input not valid, try again!")
    return user_input

def print_question(country, answers):
    print(f"What is the capital city of {country}?")
    print(f"1: {answers[0]} 2: {answers[1]} 3: {answers[2]} 4: {answers[3]}")

def print_score(game):
    print(f"Your Score: {game.score}")

