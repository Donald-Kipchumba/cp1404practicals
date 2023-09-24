print("Odd numbers between 1 and 20")
for i in range(1, 21, 2):
    print(i, end=' ')
print(" ")

print("10s between 0 to a 100")
for i in range(0, 101):
    if i % 10 == 0:
        print(i, end=' ')
print(" ")

print("printing numbers from 20 t0 0")
for i in range(20, -1, -1):
    print(i, end=' ')
print()

print("printing n stars")
numbers = int(input("Enter a random number: "))
for i in range(numbers):
    print("*", end='')
print()

print("print a right angled triangle from a number")
numbers = int(input("Enter a random number: "))
for i in range(numbers):
    for j in range(i+1):
        print("*", end='')
    print("")


