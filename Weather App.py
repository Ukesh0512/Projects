# Open Weather Map Using APIs

import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

def main():
    api_key = "b1b15e88fa797225412429c1c50c122a1"  # Replace with your actual API key
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)
    
    if "main" in weather_data and "temp" in weather_data["main"] and "humidity" in weather_data["main"] and "speed" in weather_data["wind"]:
        print("Current Weather in", city)
        print("Temperature:", weather_data["main"]["temp"], "°C")
        print("Humidity:", weather_data["main"]["humidity"], "%")
        print("Wind Speed:", weather_data["wind"]["speed"], "m/s")
    else:
        print("Failed to retrieve weather data for", city)

if __name__ == "__main__":
    main()
