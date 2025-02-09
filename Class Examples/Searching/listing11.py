def check_if_all_items_have_property(my_list, key):
    """
    Return true if at ALL items have a property.
    """
    for item in my_list:
        if item != key:
            # Found an item that didn't match. Return False.
            return False

    # Got through the entire list. There were no mis-matches.
    return True