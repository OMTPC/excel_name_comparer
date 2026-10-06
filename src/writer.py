
import pandas as pd

def write_names_to_excel(names_list: list, file_path: str, column_name: str = "Names") -> None:
    """
    Writes a list of names to an Excel file.

    Args:
        names_list (list): A list of names to write to the Excel file.
        file_path (str): The path where the Excel file will be saved.
        column_name (str): The name of the column in the Excel file. Default is "Names".

    Returns:
        None
    """
    # Create a DataFrame from the list of names
    df = pd.DataFrame({column_name: names_list})

    # Write the DataFrame to an Excel file
    df.to_excel(file_path, index=False)
    print(f"Names written successfully to {file_path}")

    