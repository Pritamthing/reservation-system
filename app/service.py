# imports 5
import Customers
import Seats
import Reservations
import Flights
import pickle

# define data structures
flights = []
customers = []
reservations = []
seats = []


def load_customer_data():
    # read customer.dat file
    with open("customers.dat", "r") as customers_file:
        for line in customers_file:
            customer_info = line.strip().split(",")
            customer = Customers.Customers(customer_info[0],
                                           customer_info[1], customer_info[2],
                                           customer_info[3], customer_info[4])
            customers.append(customer)


def load_reservation_data():
    # read reservation.dat file
    with open("reservations.dat", "r") as reservations_file:
        for line in reservations_file:
            reservation_info = line.strip().split(",")
            reservation = Reservations.Reservations(
                reservation_info[0], reservation_info[1],
                reservation_info[2], reservation_info[3])
            reservations.append(reservation)


def load_customer_data():
    # read customer.dat file
    with open("customers.dat", "r") as customers_file:
        for line in customers_file:
            customer_info = line.strip().split(",")
            customer = Customers.Customers(customer_info[0],
                                           customer_info[1], customer_info[2],
                                           customer_info[3], customer_info[4])
            customers.append(customer)


def load_reservation_data():
    # read reservation.dat file
    with open("reservations.dat", "r") as reservations_file:
        for line in reservations_file:
            reservation_info = line.strip().split(",")
            reservation = Reservations.Reservations(
                reservation_info[0], reservation_info[1],
                reservation_info[2], reservation_info[3])
            reservations.append(reservation)


def load_seats_data():
    # read seats.dat file
    with open("seats.dat", "r") as seats_file:
        for line in seats_file:
            seat_info = line.strip().split(",")
            seat = Seats.Seats(
                seat_info[0], seat_info[1], seat_info[2],
                seat_info[3])
            seats.append(seat)


def load_flight_data():
    # read flights.dat file
    with open("flights.dat", "r") as flights_file:
        for line in flights_file:
            flight_info = line.strip().split(",")
            flight = Flights.Flights(
                flight_info[0], flight_info[1], flight_info[2],
                flight_info[3], flight_info[4])
            flights.append(flight)


def init():
    load_customer_data()
    load_reservation_data()
    load_seats_data()
    load_flight_data()


def view_flights():
    print("\nAvailable Flights:")
    for flight in flights:
        print(flight.get_info())


def view_reservation():
    print("\n Reservations :")
    for reservation in reservations:
        print(reservation.get_info())

# implementation of view seats


def view_seats():
    print("\n\t Available Seats:")
    for seat in seats:
        # if seat.get_is_booked() == True:
        print(seat.get_info())


# implementation of make reservation function
def make_reservation():
    view_seats()
    choosen_flight = input("Choose your flight : ")
    choosen_seat = input("Choose your seat: ")
    option = input(
        f"Want to make reservation for new customer Y/N?: ")
    if option == "Y":
        view_customer()
        choosen_customer = input(
            f"Choose customer to book selected seat :{choosen_seat} : ")
    else:
        choosen_customer = create_customer()

    if is_reservation_valid(choosen_seat, choosen_customer):
        if any(seat.get_flight() == choosen_flight for seat in seats):
            if any(seat.get_seat_no() == choosen_seat for seat in seats):
                for seat in seats:
                    if seat.get_seat_no() == choosen_seat:
                        # get last reservation
                        last_reservation = reservations[len(reservations)-1]
                        # Define the reservation data
                        reservation = Reservations.Reservations(
                            str(int(last_reservation.get_id())+1), seat.get_flight(), choosen_customer, choosen_seat)
                        add_reservation_data(reservation)
                        update_seats_availability(reservation, "N/A")
                        break
                print(
                    f"RESERVATION SUCCESSFULL FOR THE CUSTOMER {choosen_customer}")
            else:
                print(f"Choosen seat {choosen_seat} is not found")
        else:
            print(f"Choosen flight {choosen_flight} is not found")
    else:
        print(f"Reservation for multiple flights for same customer is not allowed")
# implementation of make reservation function


def is_reservation_valid(seat, customerId):
    seat = next(filter(lambda x: x.seat_no == seat,  seats))
    # check if reservation for the selected customer is already exist
    user_reservation = None
    for reservation in reservations:
        if reservation.customer == customerId:
            user_reservation = reservation
            break
    if user_reservation is not None:
        if seat.get_flight() == reservation.get_flight():
            return True
        else:
            return False
    else:
        return True


def cancel_reservation():
    view_reservation()
    choosen_reservation = input("Choose Reservation ID to Cancel: ")
    for reservation in reservations:
        if reservation.get_id() == choosen_reservation:
            reservations.remove(reservation)
            delete_reservation(reservation)
            print(f"RESERVATION CANCELED SUCCESSFULL")
            break
    else:
        print(f"RESERVATION CANCELED FAILED")

# customer portal


def customer_portal():
    while True:
        print("\n Main Menu:")
        print("1. View Customer")
        print("2. Create Customer")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            view_customer()
        elif choice == "2":
            create_customer()
        elif choice == "3":
            update_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# view customer


def view_customer():
    print("\n\t Available Customers:")
    for customer in customers:
        print(customer.get_info())

# create a customer


def create_customer():
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    phone = input("Enter customer phone: ")
    emailaddress = input("Enter customer email: ")
    # CHECK FOR DUBLICATE EMAIL
    is_email_exists = False

    for cu in customers:
        if cu.get_email() == emailaddress:
            is_email_exists = True
            break
    if is_email_exists:
        print(
            f"Customer Already exists with provided email address: {emailaddress}")
        return
    # get the last record from data
    last_customer = customers[len(customers)-1]
    # Define the customer data
    new_customer_id = str(int(last_customer.get_id())+1)
    new_customer = [new_customer_id,
                    name, address, phone, emailaddress]

    customerslines = []
    # Load the existing customer data
    with open("customers.dat", 'r') as fp:
        # read an store all lines into list
        customerslines = fp.readlines()
    # Write file
    with open("customers.dat", 'w') as fp:
        # iterate each line
        for number, line in enumerate(customerslines):
            data = line.strip().split(",")
            fp.write(",".join(data)+"\n")
        fp.write(",".join(new_customer)+"\n")
        fp.close()
    # refresh the customer list data
    customers.clear()
    load_customer_data()
    print(
        f"Customer Created successfully with provided email address: {emailaddress}")
    return new_customer_id


def update_customer():
    id = input("Enter customer id to update: ")
    # CHECK FOR customer to update EMAIL
    customer_exists = False

    for cu in customers:
        if cu.get_id() == id:
            customer_exists = True
            break
    if customer_exists:
        name = input("Enter customer name: ")
        address = input("Enter customer address: ")
        phone = input("Enter customer phone: ")
        emailaddress = input("Enter customer email: ")
        update_customer = [str(id), name, address, phone, emailaddress]

        customerslines = []
        # Load the existing customer data
        with open("customers.dat", 'r') as fp:
            # read an store all lines into list
            customerslines = fp.readlines()
        # Write file
        with open("customers.dat", 'w') as fp:
            # iterate each line
            for number, line in enumerate(customerslines):
                data = line.strip().split(",")
                if data[0] == id:
                    fp.write(",".join(update_customer)+"\n")
                else:
                    fp.write(",".join(data)+"\n")
            fp.close()
        # refresh the customer list data
        customers.clear()
        load_customer_data()
        print(f"Customer Updated successfully with id : {id}")
    else:
        print(f"Customer Not found with if: {id}")


def delete_customer():
    id = input("Enter customer id to delete: ")
    # CHECK FOR customer to delete
    customer_exists = False
    for cu in customers:
        if cu.get_id() == id:
            customer_exists = True
            break
    if customer_exists:
        customerslines = []
        # Load the existing customer data
        with open("customers.dat", 'r') as fp:
            # read an store all lines into list
            customerslines = fp.readlines()
        # Write file
        with open("customers.dat", 'w') as fp:
            # iterate each line
            for number, line in enumerate(customerslines):
                data = line.strip().split(",")
                if data[0] != id:
                    fp.write(",".join(data)+"\n")
            fp.close()
        # refresh the customer list data
        customers.clear()
        load_customer_data()
        print(f"Customer Deleted successfully with id : {id}")
    else:
        print(f"Customer Not found with if: {id}")

# handler for reservation and cancel


def add_reservation_data(reservation_data):
    new_reservation = [reservation_data.get_id(),
                       reservation_data.get_flight(),
                       reservation_data.get_customer(),
                       reservation_data.get_seat()]
    # Load the existing customer data
    with open("reservations.dat", 'r') as fp:
        # read an store all lines into list
        reservationsLines = fp.readlines()
    # Write file
    with open("reservations.dat", 'w') as fp:
        # iterate each line
        for number, line in enumerate(reservationsLines):
            data = line.strip().split(",")
            fp.write(",".join(data)+"\n")
        fp.write(",".join(new_reservation)+"\n")
        fp.close()
    # refresh the Reservation list data
    reservations.clear()
    load_reservation_data()
    print(f"Reservation data loaded/added successfully")

# update reservation on cancelation


def delete_reservation(reservation_data):
    # Load the existing RESERVATION data
    with open("reservations.dat", 'r') as fp:
        # read an store all lines into list
        reservationsLines = fp.readlines()
    # Write file
    with open("reservations.dat", 'w') as fp:
        # iterate each line
        for number, line in enumerate(reservationsLines):
            data = line.strip().split(",")
            if data[0] != reservation_data.get_id():
                fp.write(",".join(data)+"\n")
        fp.close()
    update_seats_availability(reservation_data, "A")
    # refresh the Reservation list data
    reservations.clear()
    load_reservation_data()
    print(
        f"Reservation Canceled successfully with id : {reservation_data.get_id()}")

# update the seat availability based on the params


def update_seats_availability(choosen_reservation, is_available):
    # Load the existing RESERVATION data
    with open("seats.dat", 'r') as fp:
        # read an store all lines into list
        seatsLine = fp.readlines()
    # Write file
    with open("seats.dat", 'w') as fp:
        # iterate each line
        for number, line in enumerate(seatsLine):
            data = line.strip().split(",")
            if data[0] == choosen_reservation.get_flight() and data[2] == choosen_reservation.get_seat():
                update_seat = [data[0], data[1], data[2], is_available]
                fp.write(",".join(update_seat)+"\n")
            else:
                fp.write(",".join(data)+"\n")
        fp.close()
    seats.clear()
    load_seats_data()
    print(f"Updated seat status successfully:")
