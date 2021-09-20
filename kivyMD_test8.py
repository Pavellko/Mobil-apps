# Video Notes

# 1) theme_colors
# https://raw.githubusercontent.com/HeaTTheatR/KivyMD-data/master/gallery/kivymddoc/md-label-theme-text-color.png

# 2) Custom color
# 3) Styles
# https://raw.githubusercontent.com/HeaTTheatR/KivyMD-data/master/gallery/kivymddoc/md-label-font-style.gif
# 4) MDIcons
# https://github.com/HeaTTheatR/KivyMD/blob/master/kivymd/icon_definitions.py

# from kivy.uix.screenmanager import Screen
  
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivy.uix.boxlayout import BoxLayout

class DemoApp(MDApp):
    def build(self):
        # halign = horizontal align

        l =BoxLayout(orientation='vertical')
        label = MDLabel(text="Моя программка на KivyMD", halign="center", theme_text_color="Error",
                        font_style="Subtitle2")
        label2 = MDLabel(text="Hello world", halign="center", theme_text_color="Custom",
                        text_color=(0,0,1,1))

        label3 = MDIcon(icon="language-python", halign="center")

        l.add_widget(label)
        l.add_widget(label2)
        l.add_widget(label3)


        # 
        return l

DemoApp().run()