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
    temperature = None
    rgb_color = None
    
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "imperial"})
            if response.status_code == 200:
                weather_data = response.json()
                temperature = weather_data["main"]["temp"]  # Extract the temperature value in Fahrenheit

                # Map temperature to RGB values
                if temperature <= 45:
                    rgb_color = "rgb(0, 0, 255)"  # Cold: Blue
                elif 46 <= temperature <= 70:
                    rgb_color = f"rgb({temperature - 45}, 255, 0)"  # Mild: Green to Yellow
                else:
                    rgb_color = f"rgb(255, {255 - (temperature - 71) // 2}, 0)"  # Hot: Red to Orange

    return render_template("index.html", weather=weather_data, temperature=temperature, rgb_color=rgb_color)

if __name__ == "__main__":
    app.run(debug=True)