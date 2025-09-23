document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const cityInput = document.getElementById('city-input');
    const searchBtn = document.getElementById('search-btn');
    const locationBtn = document.getElementById('location-btn');
    const weatherDisplay = document.getElementById('weather-display');
    const weatherInfo = document.getElementById('weather-info');
    const loading = document.getElementById('loading');
    const errorMessage = document.getElementById('error-message');
    const errorText = document.getElementById('error-text');
    
    // API Configuration - Using OpenWeatherMap free tier
    // Note: For demo purposes, using a demo key. In production, you'd need your own API key
    const API_KEY = 'demo'; // Replace with actual API key for production use
    const API_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather';
    
    // Event listeners
    searchBtn.addEventListener('click', handleSearch);
    locationBtn.addEventListener('click', handleLocationSearch);
    cityInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleSearch();
        }
    });
    
    // Load default city on page load
    loadDefaultWeather();
    
    function loadDefaultWeather() {
        // Load weather for a default city (London) on page load
        fetchWeatherByCity('London');
    }
    
    function handleSearch() {
        const city = cityInput.value.trim();
        if (!city) {
            showError('Please enter a city name');
            return;
        }
        fetchWeatherByCity(city);
    }
    
    function handleLocationSearch() {
        if (!navigator.geolocation) {
            showError('Geolocation is not supported by this browser');
            return;
        }
        
        showLoading();
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const { latitude, longitude } = position.coords;
                fetchWeatherByCoordinates(latitude, longitude);
            },
            (error) => {
                hideLoading();
                switch (error.code) {
                    case error.PERMISSION_DENIED:
                        showError('Location access denied by user');
                        break;
                    case error.POSITION_UNAVAILABLE:
                        showError('Location information is unavailable');
                        break;
                    case error.TIMEOUT:
                        showError('Location request timed out');
                        break;
                    default:
                        showError('An unknown error occurred while getting location');
                        break;
                }
            }
        );
    }
    
    async function fetchWeatherByCity(city) {
        showLoading();
        
        try {
            // For demo purposes, we'll use mock data since we don't have a real API key
            // In production, uncomment the real API call below
            const weatherData = getMockWeatherData(city);
            displayWeather(weatherData);
            
            /* Real API call (uncomment for production use):
            const response = await fetch(`${API_BASE_URL}?q=${encodeURIComponent(city)}&appid=${API_KEY}&units=metric`);
            
            if (!response.ok) {
                if (response.status === 404) {
                    throw new Error('City not found');
                } else if (response.status === 401) {
                    throw new Error('Invalid API key');
                } else {
                    throw new Error('Weather data unavailable');
                }
            }
            
            const data = await response.json();
            displayWeather(data);
            */
        } catch (error) {
            hideLoading();
            showError(error.message);
        }
    }
    
    async function fetchWeatherByCoordinates(lat, lon) {
        try {
            // For demo purposes, using mock data
            const weatherData = getMockWeatherDataByCoords(lat, lon);
            displayWeather(weatherData);
            
            /* Real API call (uncomment for production use):
            const response = await fetch(`${API_BASE_URL}?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`);
            
            if (!response.ok) {
                throw new Error('Weather data unavailable');
            }
            
            const data = await response.json();
            displayWeather(data);
            */
        } catch (error) {
            hideLoading();
            showError(error.message);
        }
    }
    
    function displayWeather(data) {
        hideLoading();
        hideError();
        
        const temperature = Math.round(data.main.temp);
        const description = data.weather[0].description;
        const cityName = data.name;
        const country = data.sys.country;
        const humidity = data.main.humidity;
        const windSpeed = data.wind.speed;
        const pressure = data.main.pressure;
        const feelsLike = Math.round(data.main.feels_like);
        const weatherIcon = getWeatherIcon(data.weather[0].main);
        
        weatherInfo.innerHTML = `
            <div class="weather-main">
                <div class="weather-card">
                    <div class="weather-icon">${weatherIcon}</div>
                    <div class="city-name">${cityName}, ${country}</div>
                    <div class="temperature">${temperature}°C</div>
                    <div class="description">${description}</div>
                </div>
            </div>
            
            <div class="weather-details">
                <div class="detail-item">
                    <div class="detail-label">Feels like</div>
                    <div class="detail-value">${feelsLike}°C</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Humidity</div>
                    <div class="detail-value">${humidity}%</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Wind Speed</div>
                    <div class="detail-value">${windSpeed} m/s</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Pressure</div>
                    <div class="detail-value">${pressure} hPa</div>
                </div>
            </div>
        `;
        
        // Add animation
        weatherInfo.classList.add('animate-in');
    }
    
    function getWeatherIcon(weatherMain) {
        const icons = {
            'Clear': '☀️',
            'Clouds': '☁️',
            'Rain': '🌧️',
            'Drizzle': '🌦️',
            'Thunderstorm': '⛈️',
            'Snow': '❄️',
            'Mist': '🌫️',
            'Smoke': '🌫️',
            'Haze': '🌫️',
            'Dust': '🌫️',
            'Fog': '🌫️',
            'Sand': '🌫️',
            'Ash': '🌋',
            'Squall': '💨',
            'Tornado': '🌪️'
        };
        return icons[weatherMain] || '🌤️';
    }
    
    function showLoading() {
        loading.style.display = 'block';
        weatherDisplay.style.display = 'none';
        hideError();
    }
    
    function hideLoading() {
        loading.style.display = 'none';
        weatherDisplay.style.display = 'block';
    }
    
    function showError(message) {
        errorText.textContent = message;
        errorMessage.style.display = 'block';
        hideLoading();
    }
    
    function hideError() {
        errorMessage.style.display = 'none';
    }
    
    // Mock weather data for demonstration (remove in production)
    function getMockWeatherData(city) {
        const mockData = {
            'London': {
                name: 'London',
                sys: { country: 'GB' },
                main: { temp: 18, feels_like: 16, humidity: 65, pressure: 1013 },
                weather: [{ main: 'Clouds', description: 'partly cloudy' }],
                wind: { speed: 3.2 }
            },
            'New York': {
                name: 'New York',
                sys: { country: 'US' },
                main: { temp: 22, feels_like: 25, humidity: 58, pressure: 1015 },
                weather: [{ main: 'Clear', description: 'clear sky' }],
                wind: { speed: 2.1 }
            },
            'Paris': {
                name: 'Paris',
                sys: { country: 'FR' },
                main: { temp: 15, feels_like: 13, humidity: 72, pressure: 1008 },
                weather: [{ main: 'Rain', description: 'light rain' }],
                wind: { speed: 4.1 }
            },
            'Tokyo': {
                name: 'Tokyo',
                sys: { country: 'JP' },
                main: { temp: 25, feels_like: 28, humidity: 68, pressure: 1020 },
                weather: [{ main: 'Clear', description: 'sunny' }],
                wind: { speed: 1.8 }
            }
        };
        
        const normalizedCity = city.toLowerCase();
        for (const [key, value] of Object.entries(mockData)) {
            if (key.toLowerCase() === normalizedCity) {
                return value;
            }
        }
        
        // Default mock data for unknown cities
        return {
            name: city,
            sys: { country: 'XX' },
            main: { temp: 20, feels_like: 22, humidity: 60, pressure: 1013 },
            weather: [{ main: 'Clear', description: 'clear sky' }],
            wind: { speed: 2.5 }
        };
    }
    
    function getMockWeatherDataByCoords(lat, lon) {
        // Simple mock data based on coordinates
        return {
            name: 'Your Location',
            sys: { country: 'XX' },
            main: { temp: 19, feels_like: 21, humidity: 62, pressure: 1012 },
            weather: [{ main: 'Clouds', description: 'few clouds' }],
            wind: { speed: 2.8 }
        };
    }
    
    // Add CSS animation
    const style = document.createElement('style');
    style.innerHTML = `
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-in {
            animation: fadeIn 0.5s ease-out;
        }
    `;
    document.head.appendChild(style);
});