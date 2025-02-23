from flask import Flask, render_template, request
import requests
import json

with open("config.json") as f:
    config = json.load(f)

app = Flask(__name__)

API_KEY = config["API_KEY"]
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    weather_condition = None  # This will store the weather type (e.g., 'sunny', 'rainy', etc.)

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "imperial"})
            if response.status_code == 200:
                weather_data = response.json()
                main_weather = weather_data["weather"][0]["main"].lower()  # Extracts weather condition (e.g., "Clouds", "Rain")

                # Map OpenWeather conditions to simplified weather states
                if main_weather in ["clear"]:
                    weather_condition = "sunny"
                elif main_weather in ["clouds"]:
                    weather_condition = "cloudy"
                elif main_weather in ["rain", "drizzle"]:
                    weather_condition = "rainy"
                elif main_weather in ["thunderstorm"]:
                    weather_condition = "stormy"
                elif main_weather in ["snow"]:
                    weather_condition = "snowy"
                elif main_weather in ["mist", "smoke", "haze", "fog"]:
                    weather_condition = "foggy"
                else:
                    weather_condition = "default"

    return render_template("index.html", weather=weather_data, weather_condition=weather_condition)


if __name__ == "__main__":
    app.run(debug=True)