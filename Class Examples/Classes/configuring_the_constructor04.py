from dataclasses import dataclass


@dataclass
class Address:
    name: str = ""
    line1: str = ""
    line2: str = ""
    city: str = ""
    state: str = ""
    zip: str = ""


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
