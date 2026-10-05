
from src.reader import read_names_from_excel
from src.normalize import normalize_names_list

file_path = "data/input/adult_students_test.xlsx"

names_01 = read_names_from_excel(
    file_path="data/input/adult_students_test.xlsx",
    full_name_column="Full Name"
)

names_02 = read_names_from_excel(
    file_path="data/input/students_2C_test.xlsx",
    first_name_column="Name",
    surname_name_column="Surname"
)
normalized_names_01 = normalize_names_list(names_01)
normalized_names_02 = normalize_names_list(names_02)

print("\nFinal normalized names:")
print(normalized_names_01)
print(normalized_names_02)  

if __name__ == "__main__":
    print("\nRunning main.py script...")
    print(f"Normalized names from adult_students_test.xlsx: {normalized_names_01}")
    print(f"Normalized names from students_2C_test.xlsx: {normalized_names_02}")


