from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.display = TextInput(font_size=32, readonly=True, halign="right")
        self.add_widget(self.display)

        buttons = [
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','.','=','+'
        ]

        grid = BoxLayout()
        grid.orientation = 'vertical'

        row = BoxLayout()
        for btn in buttons:
            b = Button(text=btn, font_size=24)
            b.bind(on_press=self.on_button_press)
            row.add_widget(b)

            if len(row.children) == 4:
                grid.add_widget(row)
                row = BoxLayout()

        self.add_widget(grid)

    def on_button_press(self, instance):
        if instance.text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Error"
        else:
            self.display.text += instance.text

class CalculatorApp(App):
    def build(self):
        return Calculator()

CalculatorApp().run()