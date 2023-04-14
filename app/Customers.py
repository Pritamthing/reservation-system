class Customers:
    def __init__(self, id, name, address, phone, email):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_info(self):
        return "" + str(self.id) + ",  " + str(self.name) + ", " + self.address + ", " + self.phone + ",  " + self.email
