

import pandas as pd

from src.writer import write_names_to_excel 

def test_write_names_to_excel():
    # Test with a valid list of names and file path
    names_list = ["John Smith", "Jane Doe", "Alice Johnson"]
    file_path = "data/output/test_names.xlsx"
    column_name = "Full Name"

    write_names_to_excel(names_list, file_path, column_name)

    # Read the written Excel file to verify the contents
    df = pd.read_excel(file_path)
    read_names = df[column_name].tolist()

    print(f"Names read from written Excel: {read_names}")
    print(f"Number of names read: {len(read_names)}")
    print(read_names[:5])  # Print the first 5 names for verification

    assert read_names == names_list  # Verify that the written names match the original list    

    
