#!/usr/bin/env python3
"""
Work Late Excuse Generator

A Python program that generates random excuses for being late to work.
This tool provides various categories of believable excuses for different situations.

Usage:
    python work_late_excuses.py [category]

Categories:
    traffic - Traffic and transportation related excuses
    transport - Public transportation excuses
    personal - Personal emergencies and situations
    technical - Technology-related issues
    weather - Weather-related excuses
    family - Family emergency excuses
    health - Health-related excuses
    random - Get a random excuse from any category (default)
"""

import random
import sys


# Dictionary of work late excuses categorized by type
WORK_LATE_EXCUSES = {
    "traffic": [
        "There was a major accident on the highway that caused a 30-minute delay.",
        "Construction work blocked my usual route and GPS rerouted me through heavy traffic.",
        "A truck broke down in the tunnel and traffic was backed up for miles.",
        "There was an unexpected road closure due to a water main break.",
        "Traffic was unusually heavy due to a major event downtown.",
        "My usual route was completely blocked by emergency vehicles responding to an incident.",
        "A multi-car accident caused a complete standstill on the interstate.",
        "Road construction started earlier than announced and caught me off guard."
    ],
    
    "transport": [
        "My train was delayed by 25 minutes due to signal problems.",
        "The bus broke down and I had to wait for the next one.",
        "There was a subway delay due to a medical emergency on the tracks.",
        "My rideshare was cancelled last minute and I had to find alternative transportation.",
        "The bus was extremely crowded and I couldn't get on the first two that came.",
        "Train service was suspended temporarily due to weather conditions.",
        "My usual bus route was detoured due to a street fair I wasn't aware of.",
        "The subway system experienced technical difficulties causing major delays."
    ],
    
    "personal": [
        "I had to take my pet to the emergency vet - they ate something they shouldn't have.",
        "My elderly neighbor fell and I had to help them and wait for paramedics.",
        "I got locked out of my apartment and had to wait for the locksmith.",
        "My water heater burst and flooded my bathroom - I had to deal with the emergency.",
        "I witnessed a car accident and had to stay to give a statement to police.",
        "My apartment building's elevator broke down and I live on the 15th floor.",
        "I had to help a stranded motorist change their tire on my way to work.",
        "My building's fire alarm went off and we had to evacuate until fire department cleared us."
    ],
    
    "technical": [
        "My phone died overnight and my alarm didn't go off.",
        "There was a power outage in my neighborhood that reset all my clocks.",
        "My car wouldn't start and I had to wait for roadside assistance.",
        "My phone's alarm app crashed and didn't wake me up.",
        "The power went out and came back on, but my alarm clock was reset.",
        "My garage door opener malfunctioned and I couldn't get my car out.",
        "My phone updated overnight and somehow disabled my alarm.",
        "My car battery died and I had to get a jump start from a neighbor."
    ],
    
    "weather": [
        "The roads were extremely icy and I had to drive very slowly for safety.",
        "Heavy fog reduced visibility to almost zero, making driving dangerous.",
        "Unexpected flooding on my street made it impossible to leave on time.",
        "A tree fell across my driveway due to strong winds.",
        "The sidewalks were so icy that walking to the bus stop took twice as long.",
        "Heavy snow made driving conditions treacherous and traffic very slow.",
        "Flash flooding closed several roads on my route to work.",
        "Strong winds knocked down power lines, blocking my usual route."
    ],
    
    "family": [
        "My child woke up sick and I had to arrange last-minute childcare.",
        "I had to drive my spouse to urgent care for a medical issue.",
        "My elderly parent had a fall and I needed to check on them.",
        "There was a family emergency that required my immediate attention.",
        "My child's school called with an emergency and I had to pick them up.",
        "I had to take my family member to an urgent medical appointment.",
        "My babysitter cancelled last minute and I had to find alternative childcare.",
        "There was a medical emergency with a close family member."
    ],
    
    "health": [
        "I had a severe migraine this morning and needed time for medication to take effect.",
        "I experienced food poisoning symptoms and needed to ensure I was fit to work.",
        "I had a medical appointment that ran longer than expected.",
        "I had an allergic reaction and needed to take antihistamine and wait for it to clear.",
        "I woke up with severe back pain and needed time to manage it before driving.",
        "I had a dizzy spell and needed to ensure it was safe for me to drive.",
        "I had an asthma attack and needed time to recover before commuting.",
        "I had to go to urgent care for a minor injury that occurred this morning."
    ]
}


def get_available_categories():
    """Return a list of available excuse categories."""
    return list(WORK_LATE_EXCUSES.keys())


def get_random_excuse(category=None):
    """
    Get a random excuse from the specified category or any category if none specified.
    
    Args:
        category (str, optional): The category to get an excuse from
        
    Returns:
        tuple: (category, excuse) pair
    """
    if category and category in WORK_LATE_EXCUSES:
        excuse = random.choice(WORK_LATE_EXCUSES[category])
        return category, excuse
    elif category and category not in WORK_LATE_EXCUSES:
        return None, f"Category '{category}' not found. Available categories: {', '.join(get_available_categories())}"
    else:
        # Random category
        random_category = random.choice(get_available_categories())
        excuse = random.choice(WORK_LATE_EXCUSES[random_category])
        return random_category, excuse


def print_excuse(category, excuse):
    """Print the excuse in a formatted way."""
    print(f"\n💼 Work Late Excuse Generator 💼")
    print("=" * 40)
    print(f"Category: {category.title()}")
    print(f"Excuse: {excuse}")
    print("=" * 40)
    print("💡 Pro tip: Use responsibly and sparingly!")


def print_help():
    """Print help information about the program."""
    print(__doc__)
    print("\nAvailable categories:")
    for category in get_available_categories():
        print(f"  - {category}")
        # Show one example excuse for each category
        example = WORK_LATE_EXCUSES[category][0]
        print(f"    Example: {example}")
        print()


def main():
    """Main function to handle command line arguments and generate excuses."""
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help', 'help']:
            print_help()
            return
        
        category = sys.argv[1].lower()
        if category == 'random':
            category = None
    else:
        category = None
    
    # Generate and display excuse
    cat, excuse = get_random_excuse(category)
    
    if cat:
        print_excuse(cat, excuse)
    else:
        print(f"❌ Error: {excuse}")
        print("\nUse 'python work_late_excuses.py --help' for usage information.")


if __name__ == "__main__":
    main()