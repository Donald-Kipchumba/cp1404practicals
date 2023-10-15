"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# Iterate through the dictionary and print the states and names with formatting
for state_code, state_name in CODE_TO_NAME.items():
    print(f'{state_code} is {state_name}')

while True:
    state_code = input("Enter short state: ").upper()

    if state_code == "":
        break

    try:
        print(f'{state_code} is {CODE_TO_NAME[state_code]}')
    except KeyError:
        print("Invalid short state")
