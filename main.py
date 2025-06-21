from tkinter import *
import math
PINK = "#ffc0cb"
RED = "#ff0000"
YELLOW = "#ffff00"
GREEN = "#008000"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT = "Courier"
reps = 0
my_timer  = None


# Reset Functionality
def reset_timer():
    windows.after_cancel(my_timer)
    if reset_timer:
        my_label.config(text="Timer")
        canvas.itemconfig(timer_text, text="00:00")
        check_mark_label.config(text="")
        global reps
        reps = 0

# Windows Screen
windows = Tk()
windows.title("Pomodoro App")
windows.config(padx=100,pady=50,bg=PINK)





def timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="Break" , fg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="Break",fg=RED)
    else:
        count_down(work_sec)
        my_label.config(text = "Work" , fg=GREEN)



def count_down(count):
    minute_counter = math.floor(count / 60)
    seconds_counter = count % 60

    if seconds_counter < 10:
        seconds_counter = f"0{seconds_counter}"

    canvas.itemconfig(timer_text, text =f"{minute_counter}:{seconds_counter}")
    if count > 0:
        global my_timer
        my_timer = windows.after(1000,count_down,count-1)
    else:
        timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        check_mark_label.config(text=marks)


my_label = Label(text="Timer",font = (FONT,30,"bold"),fg=GREEN,highlightthickness=0 , bg=PINK)
my_label.grid(row=1,column=2)

# Let's Deploy Image On Screen Using Canvas Widget
canvas = Canvas(width=200,height=224,bg=PINK,highlightthickness=0)
my_image = PhotoImage(file="tomato.png")
canvas.create_image(100,115,image = my_image)
timer_text = canvas.create_text(101,140,text="00:00",font=(FONT,30,"bold"),fill="white")
canvas.grid(row=2,column=2)

# Create Start Button
start_button = Button(text="Start",font=(FONT,10,"bold"),command=timer)
start_button.grid(row=3,column=1)

# Create Reset Button
reset_button = Button(text="Reset",font=(FONT,10,"bold"),command=reset_timer)
reset_button.grid(row=3,column=3)

# Let's Create Check Mark
check_mark_label = Label(text="✔",fg=GREEN,font=(FONT,10))
check_mark_label.grid(row=4, column=2)













windows.mainloop()