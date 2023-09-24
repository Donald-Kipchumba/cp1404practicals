NAME = input("Enter your name: ")
MENU = '''Choose an option
H = Hello
G = Goodbye
Q = QUIT
'''
print(MENU)
choice = input("Enter Choice ").upper()
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {NAME}")
    if choice == 'G':
        print(f"Goodbye {NAME}")
    else:
        print("INVALID CHOICE")
    print(MENU)
    choice = input("Enter Choice ").upper()

