class Dog():

    def __init__(self, new_name):
        """ Constructor. """
        self.name = new_name


def main():
    # This creates the dog
    my_dog = Dog("Spot")

    # Print the name to verify it was set
    print(my_dog.name)

    # This line will give an error because
    # a name is not passed in.
    her_dog = Dog()


main()
