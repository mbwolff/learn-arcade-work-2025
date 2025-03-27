class Dog:
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        print(self.name + " says \"Woof\"!")


my_dog = Dog()
makenzies_dog = Dog()
makenzies_dog.name = "Kiwi"
makenzies_dog.weight = 5
makenzies_dog.age = 10

my_dog.name = "Spot"
my_dog.weight = 20
my_dog.age = 3

my_dog.bark()
makenzies_dog.bark()
