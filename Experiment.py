# Build a program to display nice messagges to the user wife in order to save him when he screw up
# Define a function to collect the user wife name and return it

def get_wife_name():
    wife_name = input("Please enter your wife name: ")
    return wife_name

import random

# Define a function to display a nice msessagge to the user wife
def display_message(wife_name):
    messages = [
        "I love you, " + wife_name + "!",
        "You are beautiful, " + wife_name + "!",
        "You are the best wife in the world, " + wife_name + "!",
        "I am so lucky to have you, " + wife_name + "!",
        "You are the love of my life, " + wife_name + "!",
        "You are my sunshine, " + wife_name + "!",
        "You are the best thing that ever happened to me, " + wife_name + "!",
        "I am so grateful for you, " + wife_name + "!",
        "You are my everything, " + wife_name + "!",
        "I cannot imagine my life without you, " + wife_name + "!",
        "You are the best wife in the world, " + wife_name + "!",
        "You are the best thing that ever happened to me, " + wife_name + "!",
        "I am so grateful for you, " + wife_name + "!",
        "You are my everything, " + wife_name + "!",
        "I cannot imagine my life without you, " + wife_name + "!"
    ]
    message = random.choice(messages)
    print(message)

# Define a main function to run the program
def main():
    wife_name = get_wife_name()
    display_message(wife_name)

# Run the program
if __name__ == "__main__":
    main()
    
