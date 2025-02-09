def check_if_one_item_has_property_v2(my_list, key):
    """
    Return true if at least one item has a
    property.
    """
    for item in my_list:
        if item == key:
            # Found an item that matched. Return True
            return True

    # Went through the whole list. Return False.
    return False
