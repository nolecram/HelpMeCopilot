import random
import json
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, static_url_path='/static')

# List of excuses categorized by type
EXCUSES = {
    "forgot_event": [
        "My phone calendar glitched and didn't send me any reminders.",
        "I set it in my calendar for next week by accident.",
        "I was preparing a surprise for you and got completely sidetracked.",
        "I had it written down but my notes app crashed and lost it.",
        "The notification came through but I was driving and forgot after.",
    ],
    "late_home": [
        "Traffic was horrible because of an accident on the highway.",
        "My boss called an emergency meeting right when I was leaving.",
        "I stopped to help someone with a flat tire.",
        "I took a detour to pick something up for us.",
        "My car wouldn't start and I had to wait for help.",
    ],
    "forgot_chore": [
        "I was in the middle of it when an urgent work email came through.",
        "I started, but then realized we were out of supplies.",
        "I thought we agreed you'd handle that this week.",
        "I did it but must have done it wrong, let me fix it.",
        "I got halfway through and got called away for something urgent.",
    ],
    "general": [
        "I was planning something special for our anniversary and got distracted.",
        "My phone died so I couldn't let you know.",
        "I thought I told you about this last week.",
        "I've been so stressed about work that it completely slipped my mind.",
        "My alarm didn't go off this morning and threw off my whole day.",
    ]
}

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/excuses')
def get_excuses():
    """Return all available excuse categories"""
    return jsonify(list(EXCUSES.keys()))

@app.route('/api/excuse/<category>')
def get_excuse(category):
    """Get a random excuse from the specified category"""
    if category in EXCUSES:
        return jsonify({
            'category': category,
            'excuse': random.choice(EXCUSES[category])
        })
    return jsonify({'error': 'Category not found'}), 404

@app.route('/api/random-excuse')
def random_excuse():
    """Get a random excuse from any category"""
    category = random.choice(list(EXCUSES.keys()))
    return jsonify({
        'category': category,
        'excuse': random.choice(EXCUSES[category])
    })

@app.route('/api/add-excuse', methods=['POST'])
def add_excuse():
    """Add a new excuse to a category"""
    data = request.get_json()
    
    if not data or 'category' not in data or 'excuse' not in data:
        return jsonify({'error': 'Missing category or excuse'}), 400
    
    category = data['category']
    excuse = data['excuse']
    
    if category not in EXCUSES:
        EXCUSES[category] = []
    
    EXCUSES[category].append(excuse)
    return jsonify({'success': True, 'message': 'Excuse added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
