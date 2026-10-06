import re
import unicodedata


def normalize_names(name: str) -> str:
    """
    Normalizes a name for comparison purposes.

    Examples:
        " José   Álvarez  "       -> "jose alvarez"
        "Caetano, ORLANDO (Mr)"   -> "orlando caetano"
        "SMITH, JOHN (Dr)"        -> "john smith"
    """

    # print(f"Original name: {name}")

    if not isinstance(name, str):
        print("Error: Input must be a string.")
        raise ValueError("Input must be a string.")

    # Remove titles in brackets e.g. (Mr), (Mrs), (Dr)
    name = re.sub(r"\([^)]*\)", "", name)

    # print(f"After removing title: {name}")

    # Handle "Surname, First Name" format
    if "," in name:
        surname, first_name = [
            part.strip()
            for part in name.split(",", 1)
        ]

        name = f"{first_name} {surname}"

        # print(f"Reordered name: {name}")

    # Lowercase and remove extra spaces
    normalized_name = " ".join(
        name.lower().strip().split()
    )

    # Remove accents
    normalized_name = (
        unicodedata
        .normalize("NFKD", normalized_name)
        .encode("ascii", "ignore")
        .decode("ascii")
    )

    # print(f"Normalized name: {normalized_name}")

    return normalized_name


def normalize_names_list(names: list) -> list:
    """
    Normalizes a list of names.
    """

    if not isinstance(names, list):
        print("Error: Input must be a list.")
        raise ValueError("Input must be a list.")

    # print(f"Normalizing {len(names)} names...")

    normalized_names = [
        normalize_names(name)
        for name in names
    ]

    print(
        f"Normalization complete. "
        f"First 5 names: {normalized_names[:5]}"
    )

    return normalized_names

# normalized_names = normalize_names_list([
#     "   John     Smith   ",
#     "José Álvarez",
#     "  Alice   Johnson  ",
#     "Caetano, ORLANDO (Mr)",
#     "SMITH, JOHN (Dr)"
# ])  

# print("\nFinal normalized names:")
# print(normalized_names) 
