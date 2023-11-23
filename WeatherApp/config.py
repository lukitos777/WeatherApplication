import requests


class Getter:
    def __int__(self) -> None:
        pass

    @staticmethod
    def get_data(city: str) -> str:
        url = 'https://api.openweathermap.org/data/2.5/weather?q='\
              + city +\
              '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

        weather_data = requests.get(url).json()

        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        return 'Temperature in ' + city + ' is ' + str(temperature) + ' C, \n' +\
            'Feels like ' + str(temperature_feels) + ' C, \n' +\
            'Humidity is ' + str(humidity) + ', \n' +\
            'wind speed is ' + str(wind_speed) + ' m/sec'