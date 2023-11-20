from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<DynamicLabelsLayout>:
    orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
        id: main
""")


class DynamicLabelsLayout(BoxLayout):
    pass


class DynamicLabelsApp(App):
    names_list = ["John", "Alice", "Bob", "Eve"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        layout = DynamicLabelsLayout()
        self.create_labels(layout)
        return layout

    def create_labels(self, layout):
        """Create labels from data and add them to the GUI."""
        for name in self.names_list:
            temp_label = Label(text=name)
            layout.ids.main.add_widget(temp_label)


if __name__ == '__main__':
    app = DynamicLabelsApp()
    app.run()
