from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from weather_api import Weather

Builder.load_string("""
<LoginScreen>
    GridLayout:
        cols:2          
        row_force_default: True
        row_default_height: 50
        spacing: 10
        padding: 20

        Label:
            text: "Username"
        TextInput:
            multiline: False
        Label:
            text: "Password"
        TextInput:
            multiline: False
            password: True
        Button:
            text: "Submit"
        Button:
            text: "Sign Up"
            on_press: root.manager.current = "signupscreen"


<SignUpScreen>
    GridLayout:
        cols:2          
        row_force_default: True
        row_default_height: 50
        spacing: 10
        padding: 20

        Label:
            text: "Username"
        TextInput:
            multiline: False
            id: username
        Label:
            text: "Password"
        TextInput:
            multiline: False
            password: True
            id: pw
        Label:
            text: "Email"
        TextInput:
            multiline: False
            id: email
        Label:
            text: "City"
        TextInput:
            multiline: False
            id: city
        Label:
            text: "State"
        TextInput:
            multiline: False
            id: state
        Button:
            text: "Submit"
            on_press: root.send_data(root.ids.username.text, root.ids.pw.text, root.ids.email.text, root.ids.city.text, root.ids.state.text)
        Button:
            text: "Go Back"
            on_press: root.manager.current = "loginscreen"

""")


class LoginScreen(Screen):
    pass

class SignUpScreen(Screen):
    def send_data(self, *args):
        weather = submit_weather(args[3], args[4])
        print(weather)


class MainApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="loginscreen"))
        sm.add_widget(SignUpScreen(name="signupscreen"))
        return sm


def submit_weather(city, state):
    weather = Weather(city, state)
    return weather


MainApp().run()