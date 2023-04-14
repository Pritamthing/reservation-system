class Seats:
    def __init__(self, flight, category, seat_no, isBooked):
        self.category = category
        self.seat_no = seat_no
        self.flight = flight
        self.isBooked = isBooked

    def get_category(self):
        return self.category

    def get_seat_no(self):
        return self.seat_no

    def get_flight(self):
        return self.flight

    def get_is_booked(self):
        return self.isBooked

    def get_info(self):
        return " " + str(self.flight) + ",  " + str(self.category) + ", " + self.seat_no + ", "+str(self.isBooked)
