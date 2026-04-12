import random
import time

num = random.randint(1, 100)
name = input("Enter your name: ")
time = time.strftime("%H:%M:%S")


print(f"Hello, {name}! Your number is: {num}")
print(f"Current time is: {time}")
