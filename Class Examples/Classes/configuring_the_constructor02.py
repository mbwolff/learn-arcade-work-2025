class Address:
    """ Hold all the fields for a mailing address. """
    def __init__(self, name, line1, line2, city, state, zip_code):
        """ Set up the address fields. """
        self.name = name
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.zip = zip_code


def print_address(address):
    """ Print an address to the screen """

    print(address.name)
    # If there is a line1 in the address, print it
    if len(address.line1) > 0:
        print(address.line1)
    # If there is a line2 in the address, print it
    if len(address.line2) > 0:
        print( address.line2 )
    print(address.city + ", " + address.state + " " + address.zip)


def main():
    # Create an address
    home_address = Address("John Smith",
                           "701 N. C Street",
                           "Carver Science Building",
                           "Indianola",
                           "IA",
                           "50125")

    # Create another address
    vacation_home_address = Address("John Smith",
                                    "1122 Main Street",
                                    "",
                                    "Panama City Beach",
                                    "FL",
                                    "32407")

    print_address(home_address)
    print()
    print_address(vacation_home_address)


main()
