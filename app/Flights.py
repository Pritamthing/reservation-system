class Flights:
    def __init__(self, flight_number, departure_time, arrival_time, origin, destination):
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.origin = origin
        self.destination = destination

    def get_flight_number(self):
        return self.flight_number

    def get_departure_time(self):
        return self.departure_time

    def get_arrival_time(self):
        return self.arrival_time

    def get_origin(self):
        return self.origin
    
    def get_destination(self):
        return self.destination

    def get_info(self):
        return f" {self.get_flight_number()} - {self.get_departure_time()} - {self.get_arrival_time()} -  {self.get_origin()} -  {self.get_destination()}"
