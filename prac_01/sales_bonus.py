
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
MENU = '''
Enter sales (enter a negative value to exit): $'''

while True:
    print(MENU)
    sales = float(input(">>>"))

    if sales < 0:
        break

    if sales >= 1000:
        bonus = (sales * 1.5)
        print("You've got a 15% bonus which amounts to {}".format(bonus))
    else:
        bonus = (sales * 0.1)
        print("You've got a 10% bonus which amounts to {:.0f}".format(bonus))
print('Thankyou')
