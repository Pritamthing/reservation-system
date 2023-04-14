class Reservations:
    def __init__(self, id, flight, customer, seat):
        self.id = id
        self.flight = flight
        self.customer = customer
        self.seat = seat

    def get_id(self):
        return self.id

    def get_flight(self):
        return self.flight

    def get_customer(self):
        return self.customer

    def get_seat(self):
        return self.seat

    def get_info(self):
        return " " + str(self.id) + ", " + str(self.flight) + ",  " + self.customer + ", " + self.seat
