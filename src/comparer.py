
def find_unmatched_names(names_a: list, names_b: list) -> list:
    """
    Find names that exist in only one list.
    
    Args:
    names_a: First list of names
    names_b: Second list of names
    
    Returns:
    Names unique to either list.
    """

    # print(f"Finding unmatched names between two lists.")
    # print(f"List A: {names_a}")
    # print(f"List B: {names_b}")

    if not isinstance(names_a, list) or not isinstance(names_b, list):
        print("Error: Both inputs must be lists.")
        raise ValueError("Both inputs must be lists.")

    set_a = set(names_a)
    set_b = set(names_b)    

    unmatched_names = list(set_a.symmetric_difference(set_b))

    print(f"Unmatched names: {unmatched_names}")

    return sorted(list(unmatched_names))


# names_a = ["john smith", "jane doe", "alice johnson"]
# names_b = ["jane doe", "bob brown", "alice johnson"]
# unmatched_names = find_unmatched_names(names_a, names_b)

