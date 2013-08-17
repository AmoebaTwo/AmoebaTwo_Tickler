#!/usr/bin/env python3

import curses
import amoebatwo

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,0,"Hit 'q' to quit")
stdscr.refresh()

m = amoebatwo.AmoebaTwo()

key = ''
while key != ord('q'):
	key = stdscr.getch()
	if key == curses.KEY_UP: 
		m.move.forwards()
	elif key == curses.KEY_LEFT:
		m.move.left()
	elif key == curses.KEY_RIGHT:
		m.move.right()
	elif key == ord('t'):
		m.lights.front.on()
	elif key == ord('y'):
		m.lights.front.off()
	elif key == ord('g'):
		m.lights.top.on()
	elif key == ord('h'):
		m.lights.top.off()
	else:
		m.move.stop()

curses.endwin()
