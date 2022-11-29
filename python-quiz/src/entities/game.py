
class Game:

    def __init__(self, player, questions):
        self.player = player
        self.rounds = 0
        self.running = False
        self.questions = questions
        self.valid = [0, 1, 2, 3, 4]

    def play(self):
        self.running = True
        while self.running:
            question = self.questions.get_questions()
            correct = question[0]
            country = question[1]
            answers = question[2]
            print(f"What is the capital of {country}?")
            print(
                f"1: {answers[0]} 2: {answers[1]} 3: {answers[2]} 4: {answers[3]}")

            user_input = self.get_input()
            if user_input == 0:
                break
            self.check_correct(correct, answers[user_input - 1])

            self.rounds += 1
            if self.rounds == 10:
                self.running = False

        print(f"Your Score: {self.player.score}")

    def check_correct(self, correct, answer):
        if correct == answer:
            print(f"You are correct. {correct} is right answer!")
            self.player.increase_score()
            print(self.player.score, "\n")
        else:
            print("Wrong answer!\n")

    def get_input(self):
        while True:
            user_input = input("Choose between 1-4, zero ends:")
            try:
                user_input = int(user_input)
            except ValueError:
                print("Input not valid, try again")
                continue
            if user_input in self.valid:
                break
            print("Input not valid, try again!")
        return user_input
