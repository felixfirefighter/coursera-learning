# template for "Stopwatch: The Game"
import simplegui

# define global variables
time_elapsed = 0
success_stop = 0
total_stop = 0
is_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = t / 600
    t = t % 600
    
    seconds = t / 10
    t = t % 10
    
    seconds_str = "0" + str(seconds) if seconds < 10 else str(seconds)
    
    return str(minutes) + ":" + seconds_str + "." + str(t)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global is_running
    is_running = True
    timer.start()

def stop_handler():
    global success_stop, total_stop, is_running
    
    timer.stop()
    
    if is_running is False:
        return
    
    if time_elapsed % 10 is 0:
        success_stop += 1
    total_stop +=1
    is_running = False
    
def reset_handler():
    global time_elapsed, success_stop, total_stop
    
    timer.stop()
    
    time_elapsed = 0
    success_stop = 0
    total_stop = 0
    
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_elapsed
    time_elapsed += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time_elapsed), (140, 200), 50, "White")
    canvas.draw_text(str(success_stop) + "/" + str(total_stop), (340, 30), 20, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 400, 400)

# register event handlers
frame.add_button("Start", start_handler, 100)
frame.add_button("Stop", stop_handler, 100)
frame.add_button("Reset", reset_handler, 100)
frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
