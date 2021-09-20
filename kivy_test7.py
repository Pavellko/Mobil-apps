# from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.boxlayout import BoxLayout

class MainApp(MDApp):
    def build(self):
        l = BoxLayout(orientation = 'vertical')
        btn = MDRectangleFlatButton(text="Hello, World", pos_hint={"center_x": 0.5, "center_y": 0.5})
        l.add_widget(btn)
        return l

MainApp().run()