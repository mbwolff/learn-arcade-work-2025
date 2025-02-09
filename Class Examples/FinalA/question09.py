class Animal:
    def __init__(self):
        self.name = ""
        self.sound = ""

    def make_sound(self):
        print(self.sound)


class Cat(Animal):
    # Cat is a child class of Animal

    def __init__(self):
        # Call the parent/super class constructor first
        Animal.__init__(self)
        # This is the constructor of the child class.
        self.sound = "Meow"


critter = Cat()
critter.name = "Fluffy"
critter.make_sound()
