
# Task 16: Weather Information Tool
# Demonstration only: these are sample values, not live weather data.

weather_data = {
    "chennai": {
        "condition": "Partly cloudy",
        "temperature": 32,
        "humidity": 65,
    },
    "coimbatore": {
        "condition": "Cloudy",
        "temperature": 28,
        "humidity": 72,
    },
    "madurai": {
        "condition": "Sunny",
        "temperature": 34,
        "humidity": 55,
    },
}


def show_weather(city):
    city = city.strip().lower()

    if city not in weather_data:
        print("City not found in the demo data.")
        print("Available cities: Chennai, Coimbatore, Madurai")
        return

    weather = weather_data[city]

    print("\n" + "=" * 35)
    print(f"DEMO WEATHER: {city.title()}")
    print("=" * 35)
    print(f"Condition:   {weather['condition']}")
    print(f"Temperature: {weather['temperature']} °C")
    print(f"Humidity:    {weather['humidity']}%")
    print("\nNote: Sample data only, not a live forecast.")


print("=" * 35)
print("WEATHER INFORMATION TOOL")
print("Type EXIT to quit.")
print("=" * 35)

while True:
    city = input("\nEnter a city: ").strip()

    if city.lower() == "exit":
        print("Goodbye!")
        break

    if city:
        show_weather(city)
    else:
        print("Please enter a city name.")
