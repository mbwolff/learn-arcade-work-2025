def check_if_one_item_is_in_room_v2(my_list, room):
    """
    Return true if at least one item has a
    property. Works the same as v1, but less code.
    """
    for item in my_list:
        if item.room == room:
            return True
    return False
