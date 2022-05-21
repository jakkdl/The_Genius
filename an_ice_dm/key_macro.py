import curses
import subprocess

key_table = {
    curses.KEY_LEFT: 'left',
    curses.KEY_RIGHT: 'right',
    curses.KEY_DOWN: 'down',
    curses.KEY_UP: 'up'
}

def main(stdscr):
    result = ''
    while True:
        c = stdscr.getch()
        if c in (10, 343): #enter
            stdscr.addstr('\n')
            result = result[:-1]
            p = subprocess.Popen(['xsel', '-ib'], stdin=subprocess.PIPE)
            p.communicate(input=result.encode())
            result = ''
        elif c in key_table:
            stdscr.addstr(key_table[c] + ' ')
            result += key_table[c] + ' '
        elif c == ord('q'):
            break
        else:
            stdscr.addstr(str(c))
            result += str(c)
            print('\a')

if __name__ == '__main__':
    curses.wrapper(main)
