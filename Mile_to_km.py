from tkinter import *

windows = Tk()
windows.minsize(600,600)
windows.title("Miles To Km Converter")

# Input Box
input_box = Entry()
input_box.grid(column=1,row=0)

# Label
my_label = Label(text="Miles",font=(20))
my_label.grid(column=2,row=0)

# is_equal_to
is_equal_to = Label(text="is equal to",font=(20))
is_equal_to.grid(column=0,row=1)


#kilometers label
kilometers_result_label = Label(text=0)
kilometers_result_label.grid(column=1,row=1)


# kilometer label
kilometer_label = Label(text="km")
kilometer_label .grid(column=2,row=1)




# Main Program
def calculation():
    miles = int (input_box.get())
    km = round (miles * 1.60934,2)
    kilometers_result_label.config (text=km)

# Calculate Button
calculate_button = Button(text = "Calculate",font=("Arial",20),command=calculation)
calculate_button.grid(column=1,row=2)




















windows.mainloop()