#!/usr/bin/env python3
"""
Weather App - A simple web application to display current weather information
"""

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    """Render the main weather app page"""
    return send_from_directory('.', 'index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files"""
    return send_from_directory('static', filename)

if __name__ == '__main__':
    print("Starting Weather App...")
    print("Open your browser and navigate to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    
    # Only enable debug mode in development environment
    import os
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)