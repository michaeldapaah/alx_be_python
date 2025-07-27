import requests

api_key = "0705ab06e2d84e4434e9d5c393b094e7"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()
if response.status_code == 200:
    print("City:", data["name"])
    print("Temperature (°C):", data["main"]["temp"])
    print("Weather Description:", data["weather"][0]["description"])
else:
    print("Error:", data.get("message", "Failed to retrieve data."))