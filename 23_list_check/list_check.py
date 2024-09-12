def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    is_list = None

    for item in lst:
        if isinstance(item, list):
            is_list = True
        else:
            is_list = False
            
    return is_list
