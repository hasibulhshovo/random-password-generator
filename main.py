# importing libraries
from random import choice
from tkinter import *

# randomly generating password (contains special characters, digits, upper and lower case letters)
def generate_password():
    lst = [(33, 91), (97, 127)]
    collect_chr = [chr(k) for i, j in lst for k in range(i, j)]
    passw = ''.join([choice(collect_chr) for i in range(0, 12)])
    return passw

# creating tkinter window
a = Tk()
# setting window title
a.title('Password Generator')
# setting window icon
a.iconphoto(False, PhotoImage(file = 'icon.png'))
# setting window size
a.geometry("300x50")

# setting a new password (on-click)
def click():
    pass_text.set(generate_password())


pass_text = StringVar()
# text field
entry = Entry(a, width=30, textvariable=pass_text)
entry.pack(side=LEFT, padx=5, pady=5)
# button
button = Button(a, text="Generate", command=click)
button.pack(side=LEFT, expand=YES)
# infinite loop
a.mainloop()