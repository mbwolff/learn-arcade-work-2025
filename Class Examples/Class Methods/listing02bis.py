class Boat:
    def __init__(self):
        self.tonnage = 0
        self.name = ""
        self.is_docked = True

    def dock(self):
        if self.is_docked:
            print("You are already docked.")
        else:
            self.is_docked = True
            print("Docking")

    def undock(self):
        if not self.is_docked:
            print("You aren't docked.")
        else:
            self.is_docked = False
            print("Undocking")


class Submarine(Boat):
    def submerge(self):
        if not self.is_docked:
            print("Submerge!")
        else:
            print("You can't do that, otherwise you will sink.")


b = Submarine()
b.dock()
b.undock()
b.undock()
b.submerge()
b.dock()
b.submerge()
b.dock()
