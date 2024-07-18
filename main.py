from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from settings import *
from kivymd.uix.card import MDCard
import requests

class WeatherCard(MDCard):
    def __init__(self, date, image, temp,desc, temp_like, w_speed,humidity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ids.image.source = f'https://openweathermap.org/img/wn/{image}@2x.png'
        self.ids.date.text = date
        self.ids.temp = f'{temp}°C'
        self.ids.temp_like = f'{temp_like}°C'
        self.ids.desc = desc.capitalize()
        self.ids.w_speed = f'Швидкість вітру {w_speed} м/с'
        self.ids.humidity = f'Вологість: {humidity}%'




class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_weather_data(self, url, city):
        api_params = {
            'q': city,
            'appid': API_KEY
        }
        data = requests.get(url, api_params)
        response = data.json()
        print(response)
        return response
    def create_weather_card(self, data):
        icon = data['weather'][0]['icon']
        desc = data['weather'][0]['description']
        temp = data['main']['temp']
        temp_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        w_speed = data['wind']['speed']
        if 'dt_text' in data:
            date = data['dt_text'][5:-3]
        else:
            date = 'Зараз'
        new_card = WeatherCard(data, icon, temp, desc, temp_like, w_speed, humidity)
        self.ids.weather_carousel.add_widget(new_card)

    def search(self):
        self.ids.weather_carousel.clear_widgets()
        city = self.ids.city.text.lower().strip()
        print(city)
        current_weather = self.get_weather_data(WEATHER_URL, city)
        self.create_weather_card(current_weather)

        forecast = self.get_weather_data(FORECAST_URL, city)
        for period in forecast['list']:
            self.create_weather_card(period)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Builder.load_file('style.kv')
        self.screen = HomeScreen(name='Home')
       
        return self.screen


MainApp().run()