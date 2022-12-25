import curses
from services.highscore_services import get_scores
from services.game_services import start_game
from services.ui_services import menu_scroll


def main(stdscr):
    """Main menu- loop functioning with up and down arrow keys and input is selected
    with linefeed, enter or space
    Is able to exit, start game and show highscores

    Args:
        stdscr (Window): Curses window initialized at index.py
    """
    row_index = 0
    main_menu(stdscr, row_index)
    while True:
        stdscr.clear()
        main_menu(stdscr, row_index)
        key = stdscr.getch()
        print(key)
        if key == 10 or key == 32 or key == curses.KEY_ENTER:
            if row_index == 2:
                break
            elif row_index == 1:
                highscores(stdscr)
            elif row_index == 0:
                start_game(stdscr)
        row_index = menu_scroll(key, row_index, 2)
        curses.beep()
        stdscr.refresh()
    


def main_menu(stdscr, row_index):
    """Prints main menu on screen, highlighting 
    current user choice.

    Args:
        stdscr (Window): Curses window
        row_index (int): Current menu row
    """
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    menu = ["Play", "Highscores", "Quit"]
    name = "Capital Game"
    a = w//2 - len(name)//2
    b = h//2 - 5
    stdscr.addstr(b,a, name, curses.A_ITALIC)
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
    for index, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + index
        if index == row_index:
            stdscr.addstr(y, x, row, curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)
    
    stdscr.refresh()


def highscores(stdscr):
    """Using get_scores function from highscore_services,
    prints scores to the screen and then waits for anykey.

    Args:
        stdscr (Window): Curses window
    """
    scores = get_scores()
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    for index, row in enumerate(scores):
        x = w//2 - len(row)//2
        y = h//2 - len(scores)//2 + index
        stdscr.addstr(y, x, row)
    stdscr.addstr(h-2, 2, "Press any key to continue")
    stdscr.getch()
    stdscr.refresh()

