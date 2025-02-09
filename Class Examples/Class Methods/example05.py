def give_money1(money):
    money += 100


class Person():
    def __init__(self):
        self.name = ""
        self.money = 0


def main():
    bob = Person()
    bob.name = "Bob"
    bob.money = 100

    give_money1(bob.money)
    print(bob.money)

main()
