import curses

# gets pressed key and current index, returns new menu index
#for either main menu or gameplay

def menu_scroll(key, row_index, length):
    if key == curses.KEY_UP and row_index > 0:
        row_index -= 1
    elif key == curses.KEY_UP and row_index == 0:
        row_index = length
    elif key == curses.KEY_DOWN and row_index < length:
        row_index += 1
    elif key == curses.KEY_DOWN and row_index == length:
        row_index = 0        
    return row_index