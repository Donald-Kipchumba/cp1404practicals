from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesToKilometresConverter(App):
    miles_output = StringProperty("0.0")

    def build(self):
        return Builder.load_file('convert_miles_km.kv')

    def handle_convert(self):
        try:
            miles = float(self.root.ids.miles_input.text)
            kilometers = miles * 1.60934
            self.miles_output = f"{kilometers:.2f}"
        except ValueError:
            self.miles_output = "Invalid Input"

    def handle_increment(self, value):
        try:
            current_miles = float(self.root.ids.miles_input.text)
            new_miles = current_miles + value
            self.root.ids.miles_input.text = str(new_miles)
            self.handle_convert()
        except ValueError:
            self.miles_output = "Invalid Input"

MilesToKilometresConverter().run()
