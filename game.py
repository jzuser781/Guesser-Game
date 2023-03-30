
import random
import tkinter as tk
import time

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")

        self.number = random.randint(1, 100)
        self.guesses = 0
        self.start_time = time.time()

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Guess", command=self.guess)
        self.button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.high_score_label = tk.Label(master, text="")
        self.high_score_label.pack()

        self.load_high_score()

    def guess(self):
        guess = int(self.entry.get())
        self.guesses += 1

        if guess < self.number:
            self.result_label.configure(text="Too low! Guess again.")
        elif guess > self.number:
            self.result_label.configure(text="Too high! Guess again.")
        else:
            elapsed_time = round(time.time() - self.start_time)
            self.result_label.configure(text=f"Congratulations! You guessed the number in {self.guesses} tries in {elapsed_time} seconds.")
            self.button.configure(state="disabled")
            self.entry.configure(state="disabled")

            self.update_high_score(elapsed_time)

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as f:
                data = f.read().split(",")
                self.high_score = int(data[0])
                self.high_score_time = int(data[1])
                self.high_score_label.configure(text=f"High Score: {self.high_score} Tries in {self.high_score_time} seconds")
        except FileNotFoundError:
            self.high_score = 0
            self.high_score_time = 0
            self.high_score_label.configure(text="")

    def save_high_score(self):
        with open("high_score.txt", "w") as f:
            f.write(f"{self.guesses},{round(time.time() - self.start_time)}")

    def update_high_score(self, elapsed_time):
        if self.guesses < self.high_score or self.high_score == 0:
            self.high_score = self.guesses
            self.high_score_time = elapsed_time
            self.high_score_label.configure(text=f"New High Score: {self.high_score} Tries in {self.high_score_time} seconds")
            self.save_high_score()

root = tk.Tk()
game = GuessingGame(root)
root.mainloop()