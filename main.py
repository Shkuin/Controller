from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, it is game controller for PC game.")


MainApp().run()