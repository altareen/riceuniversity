"""
|-------------------------------------------------------------------------------
| stopwatch_game.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Jun 24, 2015
| Execute:  python3 stopwatch_game.py
|
| This program implements the stopwatch game.
|
| Codeskulptor link:
| https://py2.codeskulptor.org/#user40_l4l9VbGgCA_7.py
|
"""

import simplegui

# define global variables
clock = 0
total = 0
success = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    return str((t/600))+':'+str((t/100)%6)+str((t/10)%10)+'.'+str(t%10)

# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    global running
    running = True
    timer.start()

def button_stop():
    global total, success, running
    timer.stop()
    if (clock%10 == 0) and running:
        success += 1
        total += 1
    elif running:
        total += 1
    running = False

def button_reset():
    global clock, total, success, running
    timer.stop()
    clock = 0
    total = 0
    success = 0
    running = False

# define event handler for timer with 0.1 sec interval
def tick():
    global clock
    clock += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(clock), (60, 110), 36, "White")
    canvas.draw_text(str(success)+"/"+str(total), (130, 40), 36, "White")

# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)

# register event handlers
frame.add_button("Start", button_start, 100)
frame.add_button("Stop", button_stop, 100)
frame.add_button("Reset", button_reset, 100)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)

# start frame
frame.start()

