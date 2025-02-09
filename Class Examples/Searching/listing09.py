def check_if_one_item_has_property_v1(my_list, key):
    """
    Return true if at least one item has a
    property.
    """
    list_position = 0
    while list_position < len(my_list) and my_list[list_position] != key:
        list_position += 1

    if list_position < len(my_list):
        # Found an item with the property
        return True
    else:
        # There is no item with the property
        return False
