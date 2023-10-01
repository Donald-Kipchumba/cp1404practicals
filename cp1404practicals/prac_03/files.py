# Task 1: Write the user's name to "name.txt"
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# Task 2: Read and print the name from "name.txt"
with open("name.txt", "r") as file:
    stored_name = file.read()
    print(f"Your name is {stored_name}")

# Task 3: Read the first two numbers from "numbers.txt" and print their sum
try:
    with open("numbers.txt", "r") as file:
        lines = file.readlines()
        num1 = int(lines[0])
        num2 = int(lines[1])
        result = num1 + num2
        print("The sum of the first two numbers is:", result)
except FileNotFoundError:
    print("File 'numbers.txt' does not exist.")

# Task 4: Read and print the total for all lines in "numbers.txt"
total = 0
try:
    with open("numbers.txt", "r") as file:
        for line in file:
            number = int(line)
            total += number
    print("The total for all numbers in numbers.txt is:", total)
except FileNotFoundError:
    print("File 'numbers.txt' does not exist.")
