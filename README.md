# CatSIM
Cataract Simulator, an application giving us the power to understand how a person suffering from cataract sees his/her surroundings. It uses OpenCV3, Python3 and Kivy.

#### Program Structure

Program is aimed to be developed in object oriented fashion. It requires Kivy/kv-lang for GUI developement (can be packaged for Windows, Linux, MacOS or Android), Python3 and OpenCV3 for simulation purpose. It has **MainApp** for calling our CataractScreen, will be made using Kivy. **Main** function for running our **MainApp**, it also has a screen monitor to monitor the display of the screen and will be used to display the GUI in a responsive manner. It will be having Kivy objects such as **Screen**, **ScreenManager**, **Image**, **Texture**, **Clock**, **Slider** and more, to carry out the whole GUI. OpenCV3 will be used to capture the video frame-by-frame with 20 frames/second and then these frames will follow a if-else program structure to display the Cataract Vision. Severity of cataract can be decided using a slider and its percentage will be displayed accordingly. This application will utilize Web-cam available in almost every laptop and will be developed on Linux machine.
