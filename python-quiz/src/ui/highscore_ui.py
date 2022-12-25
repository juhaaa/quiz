import curses
from curses import wrapper

#ui screen for user to enter name if score permits

def user_input_ui(stdscr):
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
    stdscr.clear()
    stdscr.addstr(y,x, f"Please enter a valid name!")
    stdscr.addstr(h-2, 2, "Press any key to continue")
    curses.beep()
    stdscr.getch()
    stdscr.refresh()

def name_exists(stdscr, y, x, user_name, h):
    stdscr.clear()
    stdscr.addstr(y,x, f"You did good {user_name}!")
    stdscr.addstr(h-2, 2, "Press any key to continue")
    curses.beep()
    stdscr.getch()
    stdscr.refresh()

if __name__ == "__main__":
    wrapper(user_input_ui)
