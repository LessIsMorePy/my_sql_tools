"""
    A simple function that helps you comparing what
    list elements are or not in another one.  
"""

def compare(list_origin, list_compare):
    """
        list_origin: Main list
        list_compare: List to compare in the list
                      origin if an element exist in both lists.
        return:
            *match, elements that match
            *no_match, elements that are not match
            *no_match_from_origin, elements in origin that are not match
            in the origin list.
    """
    # Empty lists
    match = []
    no_match = []
    no_match_from_origin = []

    # Evaluate if the elements from list_compare exists in the origin list
    for val in list_compare:

        if val in list_origin:
            match.append(val)
        else:
            no_match.append(val)
    # Evaluate if the elements from origin list exists in the list_compare
    for val2 in list_origin:

        if not (val2 in list_compare):
            no_match_from_origin.append(val2)

    return match, no_match, no_match_from_origin
