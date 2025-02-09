class Address:
    """ Hold all the fields for a mailing address. """
    country = "USA"
    total = 0

    def __init__(self, name, line1, line2, city, state, zip_code):
        """ Set up the address fields. """
        self.name: str = name
        self.line1: str = line1
        self.line2: str = line2
        self.city: str = city
        self.state: str = state
        self.zip: str = zip_code
        Address.total += 1


def print_address(address):
    """ Print an address to the screen """

    print(address.name)
    # If there is a line1 in the address, print it
    if len(address.line1) > 0:
        print(address.line1)
    # If there is a line2 in the address, print it
    if len(address.line2) > 0:
        print( address.line2 )
    print(address.city + ", " + address.state + " " + address.zip + " " + address.country)


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
                                    "18 rue de la Charette",
                                    "",
                                    "Paris",
                                    "",
                                    "75018")

    # we can "override" the static variable with an instance variable
    vacation_home_address.country = "France"

    print_address(home_address)
    print()
    print_address(vacation_home_address)
    print()
    print(f"Total addresses: {Address.total}")


main()
