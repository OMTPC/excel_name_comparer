
from src.reader import read_names_from_excel
from src.normalize import normalize_names_list
from src.comparer import find_unmatched_names
from src.writer import write_names_to_excel 


def main():

    file_a = "data/input/students_2C_test.xlsx"
    file_b = "data/input/adult_students_test.xlsx"

    column_name = "Name"

    names_a = read_names_from_excel(file_a, first_name_column="Name", surname_name_column="Surname")
    names_b = read_names_from_excel(file_b, full_name_column="Full Name")

    normalized_names_a = normalize_names_list(names_a)
    normalized_names_b = normalize_names_list(names_b)

    unmatched_names = find_unmatched_names(normalized_names_a, normalized_names_b)

    print(f"Unmatched names: {unmatched_names}")    

    output_file = "data/output/unmatched_names.xlsx"
    write_names_to_excel(unmatched_names, output_file, column_name="Names")

    print(f"{len(unmatched_names)} unmatched names written to {output_file}.")


if __name__ == "__main__":
    main()


# file_path = "data/input/adult_students_test.xlsx"

# names_01 = read_names_from_excel(
#     file_path="data/input/list2_names_test.xlsx",
#     full_name_column="Surname"
# )

# names_02 = read_names_from_excel(
#     file_path="data/input/students_2C_test.xlsx",
#     first_name_column="Name",
#     surname_name_column="Surname"
# )
# normalized_names_01 = normalize_names_list(names_01)
# normalized_names_02 = normalize_names_list(names_02)

# unmatched_names = find_unmatched_names(normalized_names_01, normalized_names_02)

# print("\nFinal normalized names:")
# print(normalized_names_01)
# print(normalized_names_02)  
# print(f"Unmatched names: {unmatched_names}")

# if __name__ == "__main__":
#     print("\nRunning main.py script...")
#     print(f"Normalized names from list2_names_test.xlsx: {normalized_names_01}")
#     print(f"Normalized names from students_2C_test.xlsx: {normalized_names_02}")


