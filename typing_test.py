import tkinter as tk
import random
import time
from wonderwords import RandomWord
from threading import Timer


class TypingSpeedTest:
    def __init__(self, root):
        self.random_word = RandomWord()
        self.root = root
        self.root.title("Typing Speed Test")

        # Label to display random word
        self.word_label = tk.Label(root, font=('Verdana', 30))
        self.word_label.pack(pady=20)

        # Entry for user to type the word
        self.entry = tk.Entry(root, font=('Verdana', 30), width=20)
        self.entry.pack()

        # Button to start the test
        self.start_button = tk.Button(
            root, text="Start", command=self.start_test, font=('Verdana', 20))
        self.start_button.pack(pady=20)

        # Label to display user's typing speed
        self.speed_label = tk.Label(root, font=('Verdana', 20))
        self.speed_label.pack()

        # Initialize variables
        self.current_word = ""
        self.start_time = 0
        self.end_time = 0
        self.total_time = 0
        self.start_elapsed_time = 0
        self.word_count = 0

    def generate_word(self):
        # Generate a random word from wonderwords
        self.current_word = self.random_word.word()
        self.word_label.config(text=self.current_word,
                               background="black", foreground="white")

    def start_test(self):
        # Generate a random word and change the button text to restart
        self.generate_word()
        self.start_button.pack_forget()

        # Set focus on the entry field
        self.entry.delete(0, tk.END)
        self.entry.focus()

        # Record the start time
        self.start_time = time.time()

    def restart_test(self):
        # Reset the test and start again
        self.total_time = 0
        self.speed_label.config(text="")
        self.entry.config(state='normal')
        self.start_test()

    def calculate_speed(self):
        # Calculate the speed and update the speed label
        self.end_time = time.time()
        self.total_time += self.end_time - self.start_time

        wpm = round(self.word_count / (self.total_time / 60))
        self.speed_label.config(text=f"Your typing speed is {wpm} WPM.")
        self.start_button.pack(pady=20)
        self.entry.config(state='disabled')
        self.start_button.config(text="Restart", command=self.restart_test)

    def check_word(self, event):
        # Check if the typed word matches the current word
        typed_word = self.entry.get()
        if typed_word == self.current_word:
            self.entry.delete(0, tk.END)
            self.generate_word()
        else:
            self.switch_label_bg_fg(self.word_label)

    def switch_label_bg_fg(self, label):
        bg = label.cget("background")
        fg = label.cget("foreground")
        label.configure(background=fg, foreground=bg)

    def run(self):
        # Bind the enter key to check the typed word
        self.root.bind('<Return>', self.check_word)
        self.root.after(60000, self.calculate_speed)
        self.root.mainloop()


# Create the GUI
root = tk.Tk()
app = TypingSpeedTest(root)

# Run the application
app.run()
