##Module 12
#No 1
import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
data = response.json()
print(data['value'])

#No 2
import requests

API_KEY = "895d7a41634b9afed2dc309ac10a0852"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)

    data = response.json()

    try:
        weather_description = data['weather'][0]['description']
        temperature_celsius = data['main']['temp'] - 273.15

        print(f"Weather in {city}:")
        print(f"Conditions: {weather_description.capitalize()}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
    except KeyError:
        print("Failed to retrieve valid weather data.")

if __name__ == "__main__":
    city = input("Enter the name of a city: ")
    get_weather(city)