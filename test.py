import random
import time


def random_num_gen():
    return random.randint(1, 100)


num = random_num_gen()
print("Your number is:", num)
