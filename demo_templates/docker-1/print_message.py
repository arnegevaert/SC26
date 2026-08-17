from art import tprint
import random

MESSAGES = [
    "This is some text",
    "Hello World",
    "Hello Saeyslab Conference",
]

def print_message():
    message = random.choice(MESSAGES)
    tprint(message)

if __name__ == "__main__":
    print_message()
