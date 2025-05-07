# Project Structure

This file explains the folder organization and purpose of each directory.

project-name/
├── README.md               # Overview, installation, and usage instructions
├── .gitignore              # Files and folders to ignore in Git
├── requirements.txt        # Environment or dependency file (for Python/Conda)
├── src/                    # Source code (Python, MATLAB, or Fortran)
│   ├── __init__.py         # Makes 'src' a package (Python only)
│   ├── main.py             # Entry point or main script
│   └── module_name/        # Submodules or logical components
├── data/                   # Input data, possibly with raw/processed subfolders
│   ├── raw/                # Original, immutable data dumps
│   └── clean/          # Cleaned and prepared datasets
├── notebooks/              # Jupyter or MATLAB Live Scripts for exploration
├── paper/                   # Manuscript
├── results/                # Output files such as figures, tables, logs
└── scripts/                # Functions