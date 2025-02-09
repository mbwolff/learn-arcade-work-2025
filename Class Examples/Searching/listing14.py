class AdventureObject:
    """ Class that defines an object in a text adventure game """

    def __init__(self, description, room):
        """ Constructor."""

        # Description of the object
        self.description = description

        # The number of the room that the object is in
        self.room = room

