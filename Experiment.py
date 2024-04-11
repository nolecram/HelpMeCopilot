import random

def get_random_message(name):
    messages = [
        f"{name}, you are the most beautiful person I've ever met.",
        f"{name}, your love fills my life with happiness and joy.",
        f"{name}, thank you for being my rock in times of need.",
        f"{name}, you are an amazing partner and I appreciate you.",
        f"{name}, I am grateful for every moment we share together.",
    ]
    return random.choice(messages)

def main():
    wife_name = input("Please enter your wife's name: ")
    print(get_random_message(wife_name))

if __name__ == "__main__":
    main()
