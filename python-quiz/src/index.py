from curses import wrapper
from ui.main_ui import main


if __name__ == "__main__":
    """ Starts program by initializing curses wrapper
    """
    wrapper(main)
