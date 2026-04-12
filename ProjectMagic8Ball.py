# Magic 8 Ball Project is, elif, else


# Imports
import random

# Variables
name = input("Enter your name: ")
question = input(f"Hello {name}, ask the Magic 8 Ball a question: ")
random_number = random.randint(1, 9)
answers = [
    "Yes - definitely",
    "It is decidely so",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]
answer = answers[random_number - 1]

print(f"Magic 8-Ball's answer: {answer}")
