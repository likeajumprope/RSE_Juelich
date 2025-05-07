"""
process_data.py

Cleans and processes raw data for analysis.

Usage:
    python process_data.py input.csv output.csv
"""

import pandas as pd
import sys
import os

def clean_data(input_file, output_file):
    """
    Load raw CSV data, remove missing values, and save to a new file.

    Parameters:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the cleaned CSV file.
    """
    df = pd.read_csv(input_file)
    df_clean = df.dropna()
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df_clean.to_csv(output_file, index=False)
    print(f"Cleaned data saved to: {output_file}")

#make file importable and executable
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_data.py <input.csv> <output.csv>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    clean_data(input_path, output_path)
