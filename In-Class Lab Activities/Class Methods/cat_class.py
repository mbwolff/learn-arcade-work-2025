class Cat:
    def __init__(self):
        self.color = ""
        self.name = ""
        self.weight = 0

    def meow(self):
        print(self.name + " says \"Meow\"!")


my_cat = Cat()
my_cat.name = "Fluffy"
my_cat.color = "black"
my_cat.weight = 5

another_cat = Cat()
another_cat.name = "Mittens"
another_cat.color = "orange"
another_cat.weight = 8

my_cat.meow()
another_cat.meow()
