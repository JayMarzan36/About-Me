import string, time, sys, random
from tkinter import * 
from tkinter import ttk
# create root window
root = Tk()
content = ttk.Frame(root, padding=(2, 2, 2, 2))
frame = ttk.Frame(content, borderwidth= 5, relief= 'ridge', width= 115, height= 140)
content.grid(column= 0, row= 0, sticky=(E,W))
frame.grid(column= 1, row= 0, columnspan= 2, rowspan= 3)
theme = ttk.Style()
theme.theme_use('alt')
# root window title and dimension
root.title("Pswd")
root.geometry("220x170")
root.resizable(width= False, height= False)
slider_value = StringVar()
password = []
def generate_password(length):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    pool = letters + numbers + symbols
    password = "".join(random.choices(pool, k=length))
    return password
def get_current_value():
    return f"{slider_value.get()}"
def get_slider_value(event):
    slider_value_label.configure(text = f"Length: {int(float(get_current_value()))}")
def Generate_Password():
    # print(type(get_current_value()))
    password.clear()
    length = int(float(get_current_value()))
    if length > 0:
        gen = generate_password(length)
        password.append(gen)
        # print(password)  
        # print(f"Password generated: {generated}")
        value_label.configure(text= password)
    elif length <= 0:
        value_label.configure(text= "Password")
def Copy():
    # print(f"Copied: {password[0]}")
    content.clipboard_clear()
    content.clipboard_append(password[0])
    content.update()
    content.clipboard_get()
# Text
slider_value_label = ttk.Label(content, text = "Length: 1")
slider_value_label.grid(column= 0, row= 0, padx= 5, pady= 5)
# Slider and slider related
slider = ttk.Scale(content, from_= 1, to= 100, orient = "horizontal", variable = slider_value, command= get_slider_value)
slider.grid(column= 0, row= 1, sticky= (N,S,E,W))
# Button
Generate_Password_Button = ttk.Button(content, text= 'Gen', command= Generate_Password)
Generate_Password_Button.grid(column= 0, row= 3, sticky= (N,S,E,W))
save_button = ttk.Button(content, text= 'Save to clipboard', command= Copy)
save_button.grid(column= 1, row= 3, sticky= (N,S,E,W))
value_label = ttk.Label(content, text= 'Password', wraplength= 100)
value_label.grid(column= 1, row= 0, padx= 5, pady= 5, sticky= (N,S,E,W))
frame.grid_propagate(False)
frame.columnconfigure(1, weight= 1)
frame.rowconfigure(0, weight= 1)
content.columnconfigure(1,weight= 1)
content.columnconfigure(0,weight= 1)
content.rowconfigure(0, weight= 1)
content.rowconfigure(3, weight= 1)
# Execute Tkinter
root.mainloop()