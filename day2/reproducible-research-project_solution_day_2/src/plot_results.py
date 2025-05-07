"""
plot_results.py

Generates plots from processed data.
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

def plot(input_file, output_file, x_axis="study_hours_per_day", y_axis="exam_score"):
    """
    Create and save a plot from processed data.
    
    Parameters:
        input_file (str): Path to the cleaned data file.
        output_file (str): Path to save the plot image.
        x_axis (str): Column name for the x-axis data. Defaults to 'study_hours_per_day'.
        y_axis (str): Column name for the y-axis data. Defaults to 'exam_score'.
    """
    df = pd.read_csv(input_file)
    if x_axis not in df.columns or y_axis not in df.columns:
        raise ValueError(f"Columns '{x_axis}' and/or '{y_axis}' not found in data.")

    plt.plot(df[x_axis], df[y_axis], marker='o', linestyle='none') 
    plt.title(f"{y_axis} vs {x_axis}")
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    plt.savefig(output_file)
    plt.close()
    print(f" Plot saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python plot_results.py <input.csv> <output.png>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    plot(input_file, output_file)
