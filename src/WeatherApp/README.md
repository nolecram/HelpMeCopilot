# Weather App

A simple, responsive JavaScript weather application that displays current weather information for any city.

## Features

- **Current Weather Data**: Temperature, humidity, wind speed, and atmospheric pressure
- **City Search**: Search for weather by city name
- **Location-Based Weather**: Use GPS to get weather for your current location
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Clean UI**: Modern, intuitive user interface with smooth animations
- **Weather Icons**: Visual weather representations with emoji icons

## How to Use

### Option 1: Standalone HTML (Simple)
1. Open `index.html` directly in your web browser
2. Enter a city name and click "Get Weather"
3. Or click "Use My Location" to get weather for your current location

### Option 2: Flask Server (Recommended)
1. Install Flask if you haven't already:
   ```bash
   pip install flask
   ```

2. Navigate to the WeatherApp directory:
   ```bash
   cd src/WeatherApp
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and go to: `http://localhost:5000`

## API Integration

The application is designed to work with the OpenWeatherMap API. For demonstration purposes, it currently uses mock data.

To use real weather data:

1. Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api)
2. Replace the `API_KEY` variable in `static/js/script.js` with your actual API key
3. Uncomment the real API calls in the JavaScript code

## Technical Details

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python Flask (optional)
- **API**: OpenWeatherMap API (configurable)
- **Responsive**: CSS Grid and Flexbox for responsive design
- **Geolocation**: Browser Geolocation API for location-based weather

## File Structure

```
WeatherApp/
├── index.html              # Main HTML file
├── app.py                 # Flask server (optional)
├── static/
│   ├── css/
│   │   └── styles.css     # All styling
│   └── js/
│       └── script.js      # Weather functionality
└── README.md              # This file
```

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Demo Cities

The mock data includes weather information for:
- London, GB
- New York, US
- Paris, FR
- Tokyo, JP

You can search for these cities to see different weather conditions, or enter any city name to see default weather data.

## Future Enhancements

- 5-day weather forecast
- Weather alerts and warnings
- Multiple location bookmarks
- Weather map integration
- Historical weather data