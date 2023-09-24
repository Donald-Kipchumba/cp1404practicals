while True:
    try:
        NUMBER_OF_ITEMS = int(input("Enter number of items: "))

        if NUMBER_OF_ITEMS < 0:
            print("Invalid number of items!")
            continue

        price_list = []

        total_price = 0
        for i in range(NUMBER_OF_ITEMS):
            price_of_item = float(input(f"Enter price of item, {i + 1}: "))

            if not isinstance(price_of_item, float) and not isinstance(NUMBER_OF_ITEMS, int):
                break

            price_list.append(price_of_item)
        total_price = sum(price_list)

        print(f"Total price for {NUMBER_OF_ITEMS} items is: ${total_price}")
    except ValueError as e:
        print(e)
        continue
    except KeyboardInterrupt:
        break
print("number of items and price should be a number")
