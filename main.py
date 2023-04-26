from type_test import TypeTest
from tkinter import *
from tkinter import messagebox
import time

total_elapsed_time = 0


def start_typing(event):
    global start_time
    start_time = time.time()


def stop_typing(event):
    global start_time
    elapsed_time = time.time() - start_time
    calc_elapsed_time(elapsed_time)


def calc_elapsed_time(elapsed_time):
    global total_elapsed_time
    total_elapsed_time += elapsed_time
    print("Total elapsed time", total_elapsed_time)


def end_test(event):
    total_words = len(paragraph.split(" "))
    wpm = round(total_words / (total_elapsed_time / 60))
    messagebox.showinfo(message=f"Your typing speed is {wpm} WPM.")


typetest = TypeTest()

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

messagebox.showinfo(
    message="This is a one paragraph typing test to meassure your typing speed. When ready dismiss this message and start typing the words that appear in the window.")


# Labels
paragraph = typetest.generate_paragraph()
show_paragraph = Label(text=paragraph)
show_paragraph.grid(column=0, row=0)

typing_label = Label(text="Type here: ")
typing_label.grid(column=0, row=1)

# Inputs
text_input = Entry(width=60)
text_input.grid(column=0, row=2)
text_input.focus()
text_input.bind("<Key>", start_typing)
text_input.bind("<KeyRelease>", stop_typing)
text_input.bind('<Return>', end_test)
window.mainloop()
