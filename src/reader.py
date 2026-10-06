
import pandas as pd

def read_names_from_excel(file_path: str, full_name_column: str = None, first_name_column: str = None, 
                          surname_name_column: str = None) -> list:
    """
    Reads names from an Excel file and returns them as a list.

    Args:
        file_path (str): The path to the Excel file.
        full_name_column (str): The name of the column containing the full names.
        first_name_column (str): The name of the column containing the first names.
        surname_name_column (str): The name of the column containing the surname names.

    Returns:
        list: A list of names read from the specified columns in the Excel file.
    """
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        print(f"File loaded successfully.")
        print(f"Rows found: {len(df)}")
        print(f"Columns found: {list(df.columns)}")

        # Check if the specified column exists in the DataFrame
        if full_name_column:
            if full_name_column not in df.columns:
                raise ValueError(
                    f"Column '{full_name_column}' does not exist in the Excel file.")
            
            print(f"Reading names from column: {full_name_column}")

        if first_name_column:
            if first_name_column not in df.columns:
                raise ValueError(
                    f"Column '{first_name_column}' does not exist in the Excel file.")
            
            print(f"Reading names from column: {first_name_column}")

        if surname_name_column:
            if surname_name_column not in df.columns:
                raise ValueError(
                    f"Column '{surname_name_column}' does not exist in the Excel file.")
            
            print(f"Reading names from column: {surname_name_column}")

        # Extract the names from the specified columns and convert to a list
        if full_name_column:
            names_list = df[full_name_column].dropna().astype(str).tolist()
            print(f"Names read successfully: {len(names_list)}")
        elif first_name_column and surname_name_column:
            # If both first name and surname columns are provided, combine them
            print(f"Combining names from columns: {first_name_column} and {surname_name_column}")
            names_list = (
                df[first_name_column].fillna('').astype(str)
                + ' '
                + df[surname_name_column].fillna('').astype(str)
            ).str.strip().tolist()
            print(f"Names read successfully: {len(names_list)}")
        else:
            raise ValueError("Either full_name_column or both first_name_column and surname_name_column must be provided.")

        print(f"Final list of names: {names_list[:5]}")  # Print the first 5 names for verification

        return names_list

    except Exception as e:
        print(f"An error occurred while reading the Excel file: {e}")
        return []



file_path = "data/input/list2_names_test.xlsx" 
full_name_column = 'Surname'  # Replace with the actual column name in your Excel file
# first_name_column = 'Name'
# surname_name_column = 'Surname'

read_names = read_names_from_excel(file_path, full_name_column=full_name_column)
