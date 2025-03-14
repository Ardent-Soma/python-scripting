import requests  # Import requests module

# Define API key and city
API_KEY = "94ed84d8468a170e9bc35111af0f4c7c"  # Replace with your actual API key
CITY = input('enter your city:')

# Construct the API URL
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from OpenWeather API
response = requests.get(URL)  # Send a GET request to the API
data = response.json()  # Convert response to JSON format

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract weather data from the response
    temperature = data["main"]["temp"]
    condition = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    # Print the weather information
    print(f"Weather in {CITY}: Temperature: {temperature}°C Condition: {condition} Humidity: {humidity}%")
else:
    print("Error fetching data. Check your API key or city name.")


