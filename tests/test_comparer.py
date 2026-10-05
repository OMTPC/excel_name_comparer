
from unittest import result

from src.comparer import find_unmatched_names

def test_find_unmatched_names():

    names_a = ["john smith", "jane doe", "alice johnson"]
    names_b = ["jane doe", "bob brown", "alice johnson"]

    unmatched_names = find_unmatched_names(names_a, names_b)

    print(f"Unmatched names: {unmatched_names}")

    assert unmatched_names == ["bob brown", "john smith"]

    print("Test passed: Unmatched names found successfully.")


def test_find_unmatched_names_with_empty_list():

    names_a = ["john smith", "jane doe", "alice johnson"]
    names_b = []

    unmatched_names = find_unmatched_names(names_a, names_b)

    print(f"Unmatched names with empty list: {unmatched_names}")

    assert unmatched_names == ["alice johnson", "jane doe", "john smith"]

    print("Test passed: Unmatched names found successfully with an empty list.")

def test_find_unmatched_names_identical_lists():
    names_a = ["john smith", "jane doe", "alice johnson"]
    names_b = ["john smith", "jane doe", "alice johnson"]

    unmatched_names = find_unmatched_names(names_a, names_b)

    print(f"Unmatched names with identical lists: {unmatched_names}")

    assert unmatched_names == []

    print("Test passed: No unmatched names found with identical lists.")

    