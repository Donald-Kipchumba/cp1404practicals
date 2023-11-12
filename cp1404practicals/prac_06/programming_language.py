"""
programming languages
start: 8:02am
End: 8:32am
time_taken: 32mins.
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, Dynamic Typing, Reflection={self.reflection}, First appeared in {self.year}"
