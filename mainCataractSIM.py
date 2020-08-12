"""
Email: siddharthchandragzb@gmail.com
"""

# Important Libraries to be used #
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
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

    def __init__(self, **kwargs):
        super(CataractScreen, self).__init__(**kwargs)

        # Start cv2 Camera - WebCam #
        self.capture = cv2.VideoCapture(0)

        # Create a white image #
        self.whiteImage = np.zeros([480, 640, 3], dtype="uint8")
        self.whiteImage.fill(255)

        # Make the Slider #
        self.slider = Slider(min=0, max=100, value=0, value_track=True,
                             value_track_color=hex("#2ecc71"))
        self.slider.pos = (0, -320) if (monitorHeight == 768) else (0, -520)
        self.add_widget(self.slider)

        # Label text that will be updated with slider movement #
        self.labelResult = Label(text = "Normal - No Cataract", color=hex("#2ecc71"))
        self.labelResult.font_size = 20
        self.labelResult.bold = True
        self.labelResult.pos = (0, -280) if (monitorHeight == 768) else (0, -480)
        self.add_widget(self.labelResult)
        self.slider.bind(value = self.updateResult)

        # Title of Cataract Screen #
        self.labelSim = Label(text="Cataract Simulation", color=hex("#d6eaf8"), underline=True)
        self.labelSim.font_size = 24
        self.labelSim.bold = True
        self.labelSim.pos = (0, 280) if (monitorHeight == 768) else (0, 480)
        self.add_widget(self.labelSim)

        # Close/Terminate button to close/terminate the program #
        self.closeButton = Button(text="X", color=hex("#f8f9f9"), bold=True)
        self.closeButton.font_size = 24
        self.closeButton.background_normal = ""
        self.closeButton.background_color = hex("#e74c3c")
        self.closeButton.size_hint = None, None
        self.closeButton.size = (60, 30)
        self.closeButton.pos = (1200, 700) if (monitorHeight == 768) else (1400, 900)
        self.closeButton.bind(on_press=self.closeCataractScreen)
        self.add_widget(self.closeButton)

        # Call cv2 VideoCapture read method in every 1/20 seconds #
        Clock.schedule_interval(self.update, 1.0 / 20)

    # Close/Terminate the program #
    def closeCataractScreen(self, instance):
        sys.exit(0)

    # Update the text Normal, Moderate or Severe as per slider values #
    def updateResult(self, instance, value):

        # Show Severe with its percentage #
        if int(value)>60:
            self.labelResult.text = "Severe - " + str(int(value)) + "%"
            self.labelResult.color = hex("#e74c3c")
            self.slider.value_track_color = hex("#e74c3c")

        # Show Moderate with its percentage #
        elif int(value)>10:
            self.labelResult.text = "Moderate - " + str(int(value)) + "%"
            self.labelResult.color = hex("#e67e22")
            self.slider.value_track_color = hex("#e67e22")

        # Show Normal - No Cataract #
        else:
            self.labelResult.text = "Normal - No Cataract"
            self.labelResult.color = hex("#2ecc71")
            self.slider.value_track_color = hex("#2ecc71")

    # Called after every 20 frames are read #
    def update(self, dt):
        ret, frame = self.capture.read()

        # Check if frame is returned #
        if ret:

            # Our if-elif block for changing Cataract Vision for every frame with respect to the value in Slider #
            if 10<int(self.slider.value)<=20:
                cv2.addWeighted(frame, 0.95, self.whiteImage, 0.05, 0, frame)
                frame = cv2.blur(frame, (3,3))
            elif 20<int(self.slider.value)<=30:
                cv2.addWeighted(frame, 0.9, self.whiteImage, 0.1, 0, frame)
                frame = cv2.blur(frame, (5,5))
            elif 30<int(self.slider.value)<=40:
                cv2.addWeighted(frame, 0.85, self.whiteImage, 0.15, 0, frame)
                frame = cv2.blur(frame, (7,7))
            elif 40<int(self.slider.value)<=50:
                cv2.addWeighted(frame, 0.8, self.whiteImage, 0.2, 0, frame)
                frame = cv2.blur(frame, (9,9))
            elif 50<int(self.slider.value)<=60:
                cv2.addWeighted(frame, 0.75, self.whiteImage, 0.25, 0, frame)
                frame = cv2.blur(frame, (11, 11))
            elif 60<int(self.slider.value)<=70:
                cv2.addWeighted(frame, 0.7, self.whiteImage, 0.3, 0, frame)
                frame = cv2.blur(frame, (15, 15))
            elif 70<int(self.slider.value)<=80:
                cv2.addWeighted(frame, 0.7, self.whiteImage, 0.3, 0, frame)
                frame = cv2.blur(frame, (23, 23))
            elif 80<int(self.slider.value)<=90:
                cv2.addWeighted(frame, 0.7, self.whiteImage, 0.3, 0, frame)
                frame = cv2.blur(frame, (27, 27))
            elif 90 < int(self.slider.value) <= 100:
                cv2.addWeighted(frame, 0.65, self.whiteImage, 0.35, 0, frame)
                frame = cv2.blur(frame, (31, 31))

            # Flipping our frame from web-cam to show mirror image #
            buf1 = cv2.flip(frame, 0)
            buf1 = cv2.flip(buf1, 1)
            buf = buf1.tostring()

            # Creating kivy Texture to display the result through kivy framework #
            image_texture = Texture.create(size=(640, 480), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

            # Display image from the texture #
            self.texture = image_texture


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
