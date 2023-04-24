########################################################################################################################
##                                                                                                                    ##
##                                  Ultimate Tkinter CheatSheet. - Learn basics of Tkinter.                           ##
##                                                                                                                    ##
##                         I recommend you to use "Better Comments" extension for better experience.                  ##
##                                                                                                                    ##
########################################################################################################################

#! Creating a Tkinter window and window name:

import tkinter

window = tkinter.Tk() #? Command for opening a window.

window.title("Tkinter Test") #? Displays the name of the window.

#---------------------------------

#! Printing text on the window:

text1 = tkinter.Label(window,text="Hello World!") #? Command to print text on the window.
text1.pack() #? Packaging is necessary to display the text.

text2 = tkinter.Label(window,text="Hello!",fg="red") #? The color of the text is changed with "fg".
text2.pack()

text3 = tkinter.Label(window,text="World!",fg="white",bg="black") #? The background color of the text is changed with "bg".
text3.pack()

text4 = tkinter.Label(window,text="New Text",font="Times 15 italic") #? The font, size, and weight of the text are changed with "font".
text4.pack()

text5 = tkinter.Label(window,text="New Text",font="Roboto 20 bold")
text5.pack()

#----------------------------------

#! Adding input to the window:

entry = tkinter.Entry(background="green")
entry.pack()

def get_data():
    text_on_screen.config(text=entry.get())  #? We create our data collection function. The code on the next line does the same thing.
    # text_on_screen["text"] = entry.get()

button = tkinter.Button(text="Get Data",fg="red",bg="green",command=get_data)  #? We use the button to get data.
button.pack()

text_on_screen = tkinter.Label(text="Data will come here.")  #? We create the text part where we will write the data.
text_on_screen.pack()

def delete_data():
    entry.delete(0,"end") #? The function used to delete the text inside the entry.

button_delete = tkinter.Button(text="Delete Data",fg="green",bg="red",command=delete_data) #? Button that gives the command to delete the data.
button_delete.pack()

#! Creating a password entry screen:

entry2 = tkinter.Entry(background="green",show="*") #? The show= command shows the entered characters on the screen as we want.
entry2.pack()

#----------------------------------

#! Adding buttons to the window and positioning them:

def add():
    pass

button = tkinter.Button(window,text="Add!",fg="white",bg="black",command=add) #? Adding a colored button and assigning a command.
button.pack(side=tkinter.BOTTOM,fill=tkinter.X) #? Creating and filling the position of the button.

button2 = tkinter.Button(window,text="test")
button2.pack(anchor="ne") #? "n" up, "s" down, "e" right, "w" left, "center" middle.

button3= tkinter.Button(window,text="hello")
button3.pack(padx="20",pady="100")  #? Changing the position of the button on the x and y-axis.
button3.pack(ipadx="30",ipady="20") #? Changing the size of the button on the x and y-axis.

button4 = tkinter.Button(window,text="This is a test.")
button4.place(x=150,y=40) #? Allows us to place the button anywhere on the screen. It does not move when the window size changes.

button5 = tkinter.Button(window,text="This is another test.")
button5.place(relx=0.3,rely=0.5) #? Positions the button proportionally on the x and y-axis. If the window size changes, the button's position changes.

#----------------------------------

#! Resizing and coloring the window:

window = tkinter.Tk()

window.geometry("500x400+500+200") #? Width X Height + X coordinate on the screen

window.minsize(300, 300) #? Set minimum window size

window.maxsize(10000, 100000) #? Set maximum window size

window.resizable(False, False) #? Set whether window can be resized in the X and Y axes

window.state("normal") #? Set window state to normal/iconic/zoomed

window.config(background="yellow") #? Color the window

#----------------------------------

#! Creating a check button on the window:
x = tkinter.IntVar()
x.set(0)

def check():
    if x.get() == 0:
        print("Not checked!")
    else:
        print("Checked!")

check_button = tkinter.Checkbutton(window, text="Check", fg="pink", bg="aqua", variable=x, command=check)
check_button.pack()

#----------------------------------

#! Creating radio buttons:
def control():
    if x.get() == "1":
        print("Button 1 selected.")
    elif x.get() == "2":
        print("Button 2 selected.")
    else:
        print("Buttons 1 and 2 selected.")

button = tkinter.Button(window, text="Click", foreground="black", background="aqua", activebackground="green", command=control)
button.pack()

x = tkinter.StringVar()

radio1 = tkinter.Radiobutton(window, text="radio1", activebackground="red", value="1", variable=x)
radio1.pack()   

radio2 = tkinter.Radiobutton(window, text="radio2", activebackground="red", value="2", variable=x)
radio2.pack() 

#----------------------------------

#! Displaying a message box on the screen:

from tkinter import messagebox

def message():
    messagebox.showinfo(title="Title", message="This is a message!") #? Display a message box in a new window
    messagebox.askretrycancel(title="Title2", message="This is a message with a retry button!") #? Display a message box with a retry button
    messagebox.askyesno(title="Title3", message="This is a message with yes/no buttons!") #? Display a message box with yes/no buttons
    messagebox.askquestion(title="Title4", message="This is a message with a yes/no button!") #? Display a message box with a yes/no button

message_button = tkinter.Button(window, text="Click to see a message box.", command=message)
message_button.pack()

#----------------------------------

#! Creating a combo box:
from tkinter.ttk import Combobox

cities = ["Ankara", "Istanbul", "Balikesir", "Izmir", "Burdur"]
combo_box = Combobox(window, values=cities, height=3) #? You can also write values=("1", "2", "3") without using a list.
combo_box.pack() 
#? height is the number of values that will be initially visible.
#? To get the selected value from the combo box, use "combo_box.get()" after "combo_box.pack()" in a separate line.

#----------------------------------

#! Creating a spin box:
spin_box = tkinter.Spinbox(from_=10, to=100)
spin_box.pack()

#----------------------------------

#! Running the window:
window.mainloop() #? Enters the window into a loop to keep it always on the screen.

