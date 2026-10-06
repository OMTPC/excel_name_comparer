
# import sys
# from pathlib import Path

# ROOT = Path(__file__).resolve().parent.parent
# sys.path.insert(0, str(ROOT))


import pytest

from src.reader import read_names_from_excel 

def test_read_names_from_excel():
    # Test with a valid Excel file and column name
    file_path = "data/input/adult_students_test.xlsx"
    column_name = 'Full Name'
    names = read_names_from_excel(file_path, column_name)

    print(f"Names read from Excel: {names}")
    print(f"Number of names read: {len(names)}")
    print(names[:5])  # Print the first 5 names for verification

    assert isinstance(names, list)
    assert len(names) > 0  # Assuming the test file has names

    # Test with a non-existent column name
    invalid_column_name = 'NonExistentColumn'
    names_invalid_column = read_names_from_excel(file_path, invalid_column_name)

    print (f"Names read from Excel with invalid column: {names_invalid_column}")

    assert names_invalid_column == []  # Should return an empty list for invalid column

    # Test with a non-existent file path
    invalid_file_path = "data/input/non_existent_file.xlsx"
    names_invalid_file = read_names_from_excel(invalid_file_path, column_name)

    print(f"Names read from Excel with invalid file path: {names_invalid_file}")

    assert names_invalid_file == []  # Should return an empty list for invalid file path

def test_read_names_from_two_columns():
    # Test with a valid Excel file and two column names
    file_path = "data/input/students_2C_test.xlsx"
    first_name_column = 'Name'
    surname_name_column = 'Surname'
    names = read_names_from_excel(file_path, first_name_column=first_name_column, surname_name_column=surname_name_column)

    print(f"Names read from Excel (two columns): {names}")
    print(f"Number of names read: {len(names)}")
    print(names[:5])  # Print the first 5 names for verification

    assert isinstance(names, list)
    assert len(names) > 0  # Assuming the test file has names

    # Test with a non-existent column name
    invalid_first_name_column = 'NonExistentFirstNameColumn'
    invalid_surname_name_column = 'NonExistentSurnameColumn'
    names_invalid_columns = read_names_from_excel(file_path, first_name_column=invalid_first_name_column, surname_name_column=invalid_surname_name_column)

    print(f"Names read from Excel with invalid columns: {names_invalid_columns}")

    assert names_invalid_columns == []  # Should return an empty list for invalid columns

    def test_file_not_found():
        # Test with a non-existent file path
        with pytest.raises(
            FileNotFoundError
        ):
            read_names_from_excel(
                "missing.xlsx",
                "Name"
            )
