# Excuse Generator

A Flask-based web application that generates creative excuses for various situations.

## Overview

The Excuse Generator is a humorous web application that provides random excuses categorized by situation type. It features a RESTful API and an interactive web interface.

## Features

- **Categorized Excuses**: Excuses organized by situation type:
  - `forgot_event` - Excuses for forgotten appointments or events
  - `late_home` - Excuses for arriving home late
  - `forgot_chore` - Excuses for forgotten household tasks
  - `general` - General-purpose excuses

- **RESTful API**: JSON endpoints for programmatic access
- **Interactive Web UI**: User-friendly interface for browsing and generating excuses
- **Dynamic Content**: Ability to add custom excuses via API

## Project Structure

```
ExcuseGenerator/
├── app.py              # Flask application with API endpoints
├── templates/          # HTML templates for the web interface
│   └── index.html      # Main page template
└── static/             # Static assets (CSS, JavaScript, images)
    ├── css/            # Stylesheets
    └── js/             # Client-side JavaScript
        └── script.js   # Frontend logic for excuse generation
```

## API Endpoints

### GET `/`
Renders the main web interface

### GET `/api/excuses`
Returns a list of all available excuse categories

**Response:**
```json
["forgot_event", "late_home", "forgot_chore", "general"]
```

### GET `/api/excuse/<category>`
Returns a random excuse from the specified category

**Response:**
```json
{
  "category": "forgot_event",
  "excuse": "My phone calendar glitched and didn't send me any reminders."
}
```

### GET `/api/random-excuse`
Returns a random excuse from any category

**Response:**
```json
{
  "category": "late_home",
  "excuse": "Traffic was horrible because of an accident on the highway."
}
```

### POST `/api/add-excuse`
Adds a new excuse to a category

**Request Body:**
```json
{
  "category": "forgot_event",
  "excuse": "Your custom excuse here"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Excuse added successfully"
}
```

## Installation

1. Install required dependencies:
```bash
pip install flask
```

2. Navigate to the ExcuseGenerator directory:
```bash
cd src/ExcuseGenerator
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage Examples

### Using the Web Interface
1. Open the application in your browser
2. Select a category or click "Random Excuse"
3. The excuse will be displayed on the screen

### Using the API with curl

Get a random excuse:
```bash
curl http://localhost:5000/api/random-excuse
```

Get excuses from a specific category:
```bash
curl http://localhost:5000/api/excuse/late_home
```

Add a new excuse:
```bash
curl -X POST http://localhost:5000/api/add-excuse \
  -H "Content-Type: application/json" \
  -d '{"category": "general", "excuse": "My dog ate my homework"}'
```

## Development

The application runs in debug mode by default when executed directly. For production deployment, consider using a production WSGI server like Gunicorn.

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: In-memory (excuses stored in Python dictionary)

## Notes

- Excuses are stored in memory and will reset when the application restarts
- For persistent storage, consider adding a database integration
- The application is intended for entertainment purposes only!

## Contributing

Feel free to add more excuse categories or improve the web interface. This application is part of the HelpMeCopilot learning repository.
