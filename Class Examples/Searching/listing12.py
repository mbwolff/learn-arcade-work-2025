def get_matching_items(my_list, key):
    """
    Build a brand new list that holds all the items
    that match our property.
    """
    matching_list = []
    for item in my_list:
        if item == key:
            matching_list.append(item)
    return matching_list
