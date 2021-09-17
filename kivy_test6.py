#!/usr/bin/kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


class TestApp(App):

   Window.size = (500, 500)
   title = 'Моя программка'


   def build(self):
       
       main_layout = BoxLayout(orientation = "vertical", padding=10, spacing=10)
       btn = Button(text='Hello World')
       main_layout.add_widget(btn)
       return main_layout



TestApp().run()