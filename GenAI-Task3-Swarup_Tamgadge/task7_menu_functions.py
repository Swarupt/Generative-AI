def add_price(prices_list, price):
    prices_list.append(price)


def get_average_price(prices_list):

    total = 0

    for price in prices_list:
        total = total + price

    if len(prices_list) == 0:
        return 0

    return total / len(prices_list)


def get_max_price(prices_list):

    if len(prices_list) == 0:
        return 0

    maximum = prices_list[0]

    for price in prices_list:

        if price > maximum:
            maximum = price

    return maximum


prices = []

while True:

    print("\n----- MENU -----")
    print("1 - Add price")
    print("2 - Show average price")
    print("3 - Show highest price")
    print("q - Quit")

    choice = input("Enter your choice: ")

    if choice == "1":

        price = int(input("Enter price: "))
        add_price(prices, price)
        print("Price added successfully.")

    elif choice == "2":

        if len(prices) == 0:
            print("No prices available.")
        else:
            average = get_average_price(prices)
            print("Average Price:", average)

    elif choice == "3":

        if len(prices) == 0:
            print("No prices available.")
        else:
            maximum = get_max_price(prices)
            print("Highest Price:", maximum)

    elif choice == "q":

        print("Program ended.")
        break

    else:

        print("Invalid choice.")