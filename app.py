from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_weather_data(city):
    API_KEY = '6440f9bd7422123f37a1e881b2ad6fa5'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=metric&lang=es&appid={API_KEY}'
    r = requests.get(url).json()
    return r

@app.route("/")
def index():
    data = get_weather_data('Guayaquil')
    return render_template('index.html',context=data)


if __name__ == '__main__':
    app.run(debug=True)