def check_if_all_items_are_in_room(my_list, room):
    """
    Return true if at ALL items have a property.
    """
    for item in my_list:
        if item.room != room:
            return False
    return True
