
import unicodedata

def normalize_names(name: str) -> str:
    """
    Normalizes a name by converting it to lowercase and stripping leading/trailing whitespace.

    Args:
        name (str): The name to normalize.

    Returns:
        str: The normalized name.
    """

    print (f"Normalizing name: {name}")

    if not isinstance(name, str):
        print ("Error: Input must be a string.")
        raise ValueError("Input must be a string.")

    normalized_name = " ".join(name.lower().strip().split())
    normalized_name = unicodedata.normalize('NFKD', normalized_name).encode('ascii', 'ignore').decode('ascii')

    print (f"Normalized name: {normalized_name}")

    return normalized_name

def normalize_names_list(names: list) -> list:
    """
    Normalizes a list of names.

    Args:
        names (list): A list of names to normalize.

    Returns:
        list: A list of normalized names.
    """

    print (f"Normalizing list of names: {names}")

    if not isinstance(names, list):
        print ("Error: Input must be a list.")
        raise ValueError("Input must be a list.")

    normalized_names = [normalize_names(name) for name in names]

    print (f"Normalized names: {normalized_names}")

    return normalized_names

# name = " José   Álvarez  "
# normalized_name = normalize_names(name)
