"""
Email: siddharthchandragzb@gmail.com
"""

# Important Libraries to be used #
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.slider import Slider
from kivy.utils import get_color_from_hex as hex
from kivy.uix.button import Button
from screeninfo import get_monitors
import cv2
import numpy as np
import sys

# Cataract Screen #
class CataractScreen(Screen, Image, FloatLayout):
    pass

# Check Monitor Width #
monitorWidth = str(get_monitors())[9:13]
monitorWidth = int(monitorWidth)

# Check Monitor Height #
monitorHeight = str(get_monitors())[14:18]
if monitorHeight[-1] == '+':
    monitorHeight = monitorHeight[:-1]
monitorHeight = int(monitorHeight)

sm = ScreenManager()

sm.add_widget(CataractScreen(name="CataractScreen"))

# Main App #
class MainApp(App):

    def build(self):
        return sm

# Main function #
if __name__ == "__main__":

    # Make window appear to be full screen
    Window.fullscreen = "auto"

    # Create an instance of the MainApp() and run it #
    app = MainApp()
    app.run()
