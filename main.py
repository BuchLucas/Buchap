#TechBuch


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

kv = """
<MyApp>:
    orientation: "vertical"
    Label:
        id: lb
        text: "Ola Mundo"
        font_size: "25dp"
    Button:
        size_hint_x: .5
        size_hint_y: .5
        pos_hint: {"center_x": .5,"center_y": .5}
        text: "Click Me!"
        on_release: root.click()

"""

Builder.load_string(kv)

class MyApp(BoxLayout):
    def click(self):
        self.ids.lb.text = "Eu sou Da Tech Buch"

class Construtor(App):
    def build(self):
        return MyApp()

Construtor().run()
