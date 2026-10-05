
from src.reader import read_names_from_excel
from src.normalize import normalize_names_list

file_path = "data/input/adult_students_test.xlsx"

names = read_names_from_excel(
    file_path,
    full_name_column="Full Name",
    #first_name_column="Name",
    #surname_name_column="Surname"
)

normalized_names = normalize_names_list(names)

print("\nFinal normalized names:")
print(normalized_names)
