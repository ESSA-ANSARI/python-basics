# Day 9 - API Requests: Live Weather App
import requests

API_KEY = "8e41116a853137332f009f1debc2222a"  # Replace with your OpenWeather API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']

        print(f"\n🌍 City: {city}")
        print(f"🌡 Temperature: {temp}°C")
        print(f"☁️ Condition: {weather.capitalize()}")
        print(f"💧 Humidity: {humidity}%")
    else:
        # Show demo data when API fails
        print(f"❌ API Error: {data.get('message', 'API key invalid')}")
        print("📝 Showing DEMO data instead:")
        print(f"\n🌍 City: {city}")
        print(f"🌡 Temperature: 22.5°C")
        print(f"☁️ Condition: Partly cloudy")
        print(f"💧 Humidity: 68%")
        print("💡 Get a valid API key from openweathermap.org to see real data!")

while True:
    city = input("\nEnter city name (or 'exit' to quit): ").strip()
    if city.lower() == "exit":
        print("👋 Goodbye!")
        break
    get_weather(city)
