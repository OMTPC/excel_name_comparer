
# import sys
# from pathlib import Path

# ROOT = Path(__file__).resolve().parent.parent
# sys.path.insert(0, str(ROOT))

from src.normalize import normalize_names, normalize_names_list


def test_lower_case():

    assert normalize_names(
        "John Smith"
    ) == "john smith"

    print ("Test passed: Lowercase conversion successful.")
    print (f"Normalized name: {normalize_names('John Smith')}")


def test_remove_spaces():

    assert normalize_names(
        "   John     Smith   "
    ) == "john smith"

    print ("Test passed: Leading/trailing and multiple spaces removed successfully.")
    print (f"Normalized name: {normalize_names('   John     Smith   ')}")


def test_already_clean():

    assert normalize_names(
        "john smith"
    ) == "john smith"

    print ("Test passed: Already clean name remains unchanged.")
    print (f"Normalized name: {normalize_names('john smith')}")

def test_remove_accents():

    assert normalize_names(
        "José Álvarez"
    ) == "jose alvarez"

    print ("Test passed: Accents removed successfully.")
    print (f"Normalized name: {normalize_names('José Álvarez')}")

def test_normalize_list():
    
    names = ["   John     Smith   ", "José Álvarez", "  Alice   Johnson  "]
    expected_normalized_names = ["john smith", "jose alvarez", "alice johnson"]

    assert normalize_names_list(names) == expected_normalized_names

    print ("Test passed: List of names normalized successfully.")
    print (f"Normalized names list: {normalize_names_list(names)}")
    


