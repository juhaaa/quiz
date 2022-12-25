import curses
from curses import wrapper



def user_input_ui(stdscr):
    """Ui screen for user to input name, displays until name is entered
    correctly.

    Args:
        stdscr (Window): Curses window

    Returns:
        str: players name
    """
    user_name = ""
    while True:
        if len(user_name) > 0:
            name_exists(stdscr, y, x, user_name, h)
            return user_name
        curses.echo()
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        name_string = "Please enter your name:"
        x = w//2 - len(name_string)//2
        y = h//2
        stdscr.addstr(y-2,x, "You made it to the list!", curses.A_BLINK)
        stdscr.addstr(y,x, name_string)
        stdscr.move(y+1,x)
        user_name = stdscr.getstr(15).decode()
        if user_name == "":
            not_name(stdscr, y, x, h)
    
def not_name(stdscr, y, x, h):
    """Reminder to enter a valid name.

    Args:
        stdscr (Window): Curses window
        y (int): terminal center y
        x (int): terminal center x
        h (int): terminal max heigth
    """
    stdscr.clear()
    stdscr.addstr(y,x, f"Please enter a valid name!")
    stdscr.addstr(h-2, 2, "Press any key to continue")
    curses.beep()
    stdscr.getch()
    stdscr.refresh()

def name_exists(stdscr, y, x, user_name, h):
    """Ui screen to congratulate player.

    Args:
        stdscr (Window): Curses window
        y (int): terminal center y
        x (int): terminal center x
        h (int): terminal max heigth
        user_name (str): players name.
    """
    stdscr.clear()
    stdscr.addstr(y,x, f"You did good {user_name}!")
    stdscr.addstr(h-2, 2, "Press any key to continue")
    curses.beep()
    stdscr.getch()
    stdscr.refresh()
