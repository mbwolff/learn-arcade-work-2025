def check_if_one_item_is_in_room_v1(my_list, room):
    """
    Return true if at least one item has a
    property.
    """
    i = 0
    while i < len(my_list) and my_list[i].room != room:
        i += 1

    if i < len(my_list):
        # Found an item with the property
        return True
    else:
        # There is no item with the property
        return False
