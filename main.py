from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Builder.load_file('style.kv')
        self.screen = HomeScreen(name='Home')
       
        return self.screen


MainApp().run()