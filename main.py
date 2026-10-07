
from src.reader import read_names_from_excel
from src.normalize import normalize_names_list
from src.comparer import find_unmatched_names
from src.writer import write_names_to_excel 


def main():

    file_a = "data/input/year2_SMT_PARA_07_10_2026.xlsx"
    file_b = "data/input/Book13.xlsx"

    column_name = "Name"

    names_a = read_names_from_excel(file_a, full_name_column="Full Name")
    names_b = read_names_from_excel(file_b, first_name_column="Name", surname_name_column="Surname")

    normalized_names_a = normalize_names_list(names_a)
    normalized_names_b = normalize_names_list(names_b)

    unmatched_names = find_unmatched_names(normalized_names_a, normalized_names_b)

    print(f"Unmatched names: {unmatched_names}")    

    output_file = "data/output/unmatched_names.xlsx"
    write_names_to_excel(unmatched_names, output_file, column_name="Names")

    print(f"{len(unmatched_names)} unmatched names written to {output_file}.")


if __name__ == "__main__":
    main()

