from type_test import TypeTest
from tkinter import *
from tkinter import messagebox
import time


typetest = TypeTest()

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

messagebox.showinfo(
    message="This is a one paragraph typing test to meassure your typing speed. When ready dismiss this message and start typing the words that appear in the window.")


# Labels
show_paragraph = Label(text=typetest.generate_paragraph())
show_paragraph.grid(column=0, row=0)

typing_label = Label(text="Type here: ")
typing_label.grid(column=0, row=1)

# Inputs
text_input = Entry(width=60)
text_input.grid(column=0, row=2)
text_input.focus()
text_input.bind("<KeyPress>", print)

window.mainloop()
