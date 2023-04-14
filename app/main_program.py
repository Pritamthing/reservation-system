
import service


def staff_operations():
    while True:
        print("\n Staff Actions:")
        print("1. View Flights")
        print("2. Make Reservation")
        print("3. View Reservation")
        print("4. Cancel Reservation")
        print("5. Customer")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            service.view_flights()
        elif choice == "2":
            service.make_reservation()
        elif choice == "3":
            service.view_reservation()
        elif choice == "4":
            service.cancel_reservation()
        elif choice == "5":
            service.customer_portal()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def customer_operations():
    while True:
        print("\n Customer Actions:")
        print("1. View Flights")
        print("2. View Seats Availability")
        print("3. View Reservation")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            service.view_flights()
        elif choice == "2":
            service.view_seats()
        elif choice == "3":
            service.view_reservation()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def main_menu():
    while True:
        print("\n Choose Customer/Staff:")
        print("1. Customer")
        print("2. Staff")
        print("3. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            customer_operations()
        elif choice == "2":
            password = input("Enter password:")
            if password == "staff":
                staff_operations()
            else:
                print("Wrong password! Please enter correct password")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# start program
if __name__ == "__main__":
    service.init()
    main_menu()
