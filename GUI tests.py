from tkinter import *
from tkinter import colorchooser

My_window = Tk()
My_window.title("inital_maker beta build")
My_window.geometry("800x600")
User = int(input("1 = light mode 2 = dark mode"))
def background_colour():
    if User == 1:
        My_window.configure(bg='#FFFFFF')
    elif User == 2:
        My_window.configure(bg='#000000')
    else:
        print("Not a valid input!")
        break
    
background_colour()    
My_window.mainloop()