import curses
from curses import wrapper

#ui screen for user to enter name if score permits

def user_input_ui(stdscr):
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
    stdscr.clear()
    stdscr.addstr(y,x, f"You did good {user_name}!")
    stdscr.getch()
    stdscr.refresh()
    return user_name

if __name__ == "__main__":
    wrapper(user_input_ui)
