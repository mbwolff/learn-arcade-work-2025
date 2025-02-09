def get_items_in_room(my_list, room):
    """
    Build a brand new list that holds all the items
    that match our property.
    """
    matching_list = []
    for item in my_list:
        if item.room == room:
            matching_list.append(item)
    return matching_list
