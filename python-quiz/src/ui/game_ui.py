import curses
from services.ui_services import menu_scroll

def game_interface_main(stdscr,country, answers, score):
    row_index = 0
    h, w = stdscr.getmaxyx()
    game_interface_choices(stdscr, row_index,country, answers, score)
    while True:
        stdscr.clear()
        game_interface_choices(stdscr, row_index, country, answers, score)
        score_print = f"Score: {score}"
        stdscr.addstr(h-5,w-5-len(score_print), score_print, curses.A_ITALIC)
        key = stdscr.getch()
        print(key)
        if key == 10 or key == 32 or key == curses.KEY_ENTER:
            return row_index + 1
        row_index = menu_scroll(key, row_index, 3)
        stdscr.refresh()


def game_interface_choices(stdscr, row_index, country, answers, score):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    menu = answers
    question = f"What is the Capital city of {country}?"
    a = w//2 - len(question)//2
    b = h//2 - 5
    stdscr.addstr(b,a, question, curses.A_ITALIC)
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
    for index, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + index
        if index == row_index:
            stdscr.addstr(y, x, row, curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)
    curses.beep()
    stdscr.refresh()

# these two display the outcome of players answers

def ui_answer(stdscr, correct_string):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(correct_string)//2
    y = h//2
    stdscr.addstr(y, x, correct_string, curses.A_ITALIC)
    curses.beep()
    stdscr.refresh()
    stdscr.getch()
