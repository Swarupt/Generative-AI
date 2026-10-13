orders = []

while True:

    print("\n----- MENU -----")
    print("1 - Add order amount")
    print("2 - Show all orders and totals")
    print("q - Quit")

    choice = input("Enter your choice: ")

    if choice == "1":

        order_amount = int(input("Enter order amount: "))
        orders.append(order_amount)

        print("Order added successfully.")

    elif choice == "2":

        if len(orders) == 0:
            print("No orders available.")
            continue

        total_revenue = 0

        print("\nOrder Amount\tDiscount\tFinal Amount")

        for order_amount in orders:

            if order_amount >= 2000:
                discount = order_amount * 15 / 100
            elif order_amount >= 1500:
                discount = order_amount * 10 / 100
            elif order_amount >= 1000:
                discount = order_amount * 7 / 100
            else:
                discount = 0

            final_amount = order_amount - discount

            print(order_amount, "\t\t", discount, "\t\t", final_amount)

            total_revenue = total_revenue + final_amount

        print("Total Revenue:", total_revenue)

    elif choice == "q":

        print("Program ended.")
        break

    else:

        print("Invalid choice. Please try again.")
        continue