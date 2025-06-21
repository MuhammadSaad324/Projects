from tkinter import *

from names_data import *
import random
windows = Tk()
windows.title("My First GUI")
windows.minsize(600,600)

# Let's Create a Label
my_label = Label(text= "I Am A Label.",font = ("Noto Serif",30))
my_label.config(text = "AlphaGo")
my_label.grid(column = 0 , row = 0)


# Let's create a text input and add eventListener
def click_button () :
    my_label ["text"] = my_entry.get()
    print("Hello World!")
my_button = Button(text = "Click Me",font = "Arial",command = click_button)
my_button.grid(column= 2 , row= 2)

# Let's Create EntryWay
my_entry = Entry(width = 40)
my_entry.grid(row= 3 , column= 4)

# New Button
new_button = Button(text = "New Button",font = "Arial")
new_button.grid(row= 0 , column = 2)
# # Text
# my_text = Text()
# my_text.focus()
# my_text.insert(END, "Example of multi-line text entry.")
# print(my_text.get("1.0", END))
# my_text.pack()
#
# # Spinbox
# def spin_box_used () :
#     print(my_spin_boxes.get())
# my_spin_boxes = Spinbox(from_= 0 , to = 20 , command = spin_box_used)
# my_spin_boxes.pack()
#
# # Scale
# def scale_used (value):
#     print(value)
# scale = Scale(from_= 0, to = 100 , command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

windows.mainloop()