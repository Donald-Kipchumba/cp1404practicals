"""
programming languages
start: 9:02am
End: 9:15am
time_taken: 13mins.
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]

print("\nThe dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
