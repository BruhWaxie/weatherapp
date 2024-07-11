from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from settings import *
from kivymd.uix.card import MDCard
import requests

class WeatherCard(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
    

    def search(self):
        city = self.ids.city.text.lower().strip()
        print(city)
        current_weather = self.get_weather_data(WEATHER_URL, city)
        temp = current_weather['main']["temp"]
        self.ids.content_text.text = f'{temp}°C'

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Builder.load_file('style.kv')
        self.screen = HomeScreen(name='Home')
       
        return self.screen


MainApp().run()