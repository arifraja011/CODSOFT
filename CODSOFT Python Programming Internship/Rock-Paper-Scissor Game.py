import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        # User's choice buttons
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play('rock'), font=('Arial', 14, 'bold'), bg='brown', fg='white')
        self.rock_button.grid(row=0, column=0, padx=10, pady=10)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play('paper'), font=('Arial', 14, 'bold'), bg='blue', fg='white')
        self.paper_button.grid(row=0, column=1, padx=10, pady=10)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play('scissors'), font=('Arial', 14, 'bold'), bg='green', fg='white')
        self.scissors_button.grid(row=0, column=2, padx=10, pady=10)

        # Labels to show results
        self.user_choice_label = tk.Label(self.root, text="Your Choice: ", font=('Arial', 12, 'bold'))
        self.user_choice_label.grid(row=1, column=0, padx=10, pady=10)

        self.computer_choice_label = tk.Label(self.root, text="Computer's Choice: ", font=('Arial', 12, 'bold'))
        self.computer_choice_label.grid(row=1, column=1, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="", font=('Arial', 12, 'bold'))
        self.result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.score_label = tk.Label(self.root, text="Score - Your Score: 0 Computer Score: 0", font=('Arial', 12, 'bold'))
        self.score_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        self.user_choice_label.config(text=f"Your Choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
        
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1
        
        self.result_label.config(text=result)
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score - Your Score: {self.user_score} Computer Score: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
