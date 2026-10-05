
import pandas as pd

def read_names_from_excel(file_path: str, column_names: str) -> list:
    """
    Reads names from an Excel file and returns them as a list.

    Args:
        file_path (str): The path to the Excel file.
        column_names (str): The name of the column containing the names.

    Returns:
        list: A list of names read from the specified column in the Excel file.
    """
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        print(f"File loaded successfully.")
        print(f"Rows found: {len(df)}")
        print(f"Columns found: {list(df.columns)}")

        # Check if the specified column exists in the DataFrame
        if column_names not in df.columns:
            raise ValueError(f"Column '{column_names}' does not exist in the Excel file.")

        print(f"Reading names from column: {column_name}")

        # Extract the names from the specified column and convert to a list
        names_list = df[column_names].dropna().tolist()

        print(f"Names read successfully: {len(names_list)}")

        return names_list

    except Exception as e:
        print(f"An error occurred while reading the Excel file: {e}")
        return []



file_path = "data/input/adult_students_test.xlsx" 
column_name = 'Full Name' 

read_names_from_excel(file_path, column_name)
