#!/usr/bin/env python3
"""
Test file for Weather App functionality
"""

import unittest
import sys
import os

# Add the WeatherApp directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'WeatherApp'))

from app import app

class TestWeatherApp(unittest.TestCase):
    def setUp(self):
        """Set up test client"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_index_page_loads(self):
        """Test that the main page loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Daily Weather Report', response.data)
        self.assertIn(b'Get the current weather conditions', response.data)

    def test_static_css_loads(self):
        """Test that CSS file is accessible"""
        response = self.client.get('/static/css/styles.css')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'weather-container', response.data)

    def test_static_js_loads(self):
        """Test that JavaScript file is accessible"""
        response = self.client.get('/static/js/script.js')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'fetchWeatherByCity', response.data)

    def test_html_structure(self):
        """Test that HTML contains required elements"""
        response = self.client.get('/')
        html_content = response.data.decode('utf-8')
        
        # Check for essential HTML elements
        self.assertIn('id="city-input"', html_content)
        self.assertIn('id="search-btn"', html_content)
        self.assertIn('id="location-btn"', html_content)
        self.assertIn('id="weather-display"', html_content)
        self.assertIn('Weather App', html_content)

if __name__ == '__main__':
    unittest.main()