import curses



def menu_scroll(key, row_index, length):
    """Gets pressed key and current index, returns new menu index
    for either main menu or gameplay
    Args:
        key (int): key pressed
        row_index (int): index of current row
        length (int): menu- length

    Returns:
        int: New menu row index
    """

    if key == curses.KEY_UP and row_index > 0:
        row_index -= 1
    elif key == curses.KEY_UP and row_index == 0:
        row_index = length
    elif key == curses.KEY_DOWN and row_index < length:
        row_index += 1
    elif key == curses.KEY_DOWN and row_index == length:
        row_index = 0
    return row_index
