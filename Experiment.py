import random

def get_nice_messages():
    messages = [
        "You're an amazing person and I'm lucky to have you in my life.",
        "I love you more than words can express.",
        "Thank you for being the amazing person you are.",
        "You brighten my day every time I see you.",
        "Your love and support mean the world to me."
    ]
    return messages

def main():
    wife_name = input("Please enter your wife's name: ")
    messages = get_nice_messages()
    random_message = random.choice(messages)
    print(f"Dear {wife_name}, {random_message}")

if __name__ == "__main__":
    main()
