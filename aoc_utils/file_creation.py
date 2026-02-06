"""
File for creating AOC files for me to use, automates some of the basics like adding in the data import, main methods for p1 and p2.

To use this file, running for 2015:
python aoc_utils/file_creation.py 2015

"""


import sys
from pathlib import Path

# --- CONFIGURATION: EDIT THIS TEMPLATE FOR FUTURE YEARS ---
TEMPLATE = """from aoc_utils import data_import

raw_data = data_import.get_input()
data_import.preview()

def data_prep(data):
    pass

def main_p1(data):
    pass

def main_p2(data):
    pass

if __name__ == "__main__":
    # main_p1(raw_data)
    # main_p2(raw_data)   
    pass
"""
# -----------------------------------------------------------

def get_repo_root():
    """Finds the root 'aoc' folder based on this file's location."""
    # Assuming this file is in /home/ryan/repos/aoc/aoc_utils/file_creation.py
    # .parent = aoc_utils, .parent.parent = aoc
    return Path(__file__).parent.parent.resolve()

def setup_year(year):
    """
    Creates the folder structure and python files for a given year.
    - Creates 'year' folder.
    - Creates 'year/input' folder.
    - Creates day01.py to day25.py (or day12.py for 2025+).
    """
    root = get_repo_root()
    year_path = root / str(year)
    input_path = year_path / "input"

    # 1. Create Directories
    print(f"Checking directories for {year}...")
    if not year_path.exists():
        year_path.mkdir(parents=True)
        print(f"  Created folder: {year_path}")
    
    if not input_path.exists():
        input_path.mkdir(parents=True)
        print(f"  Created folder: {input_path}")

    # 2. Determine Day Count
    # "Default to 25 days, but from 2025 on it's 12 days"
    if year >= 2025:
        total_days = 12
    else:
        total_days = 25

    print(f"Generating {total_days} days for {year}...")

    # 3. Create Files
    files_created = 0
    for day in range(1, total_days + 1):
        filename = f"day{day:02}.py"
        file_path = year_path / filename

        if not file_path.exists():
            file_path.write_text(TEMPLATE)
            print(f"  + Created {filename}")
            files_created += 1
        else:
            # We don't print anything for skipped files to keep output clean,
            # unless you really want to know.
            pass

    print(f"Done. {files_created} new files created in {year_path}")

if __name__ == "__main__":
    # Allows you to run this script directly from the terminal
    # Usage: python3 aoc_utils/file_creation.py 2015
    if len(sys.argv) > 1:
        try:
            target_year = int(sys.argv[1])
            setup_year(target_year)
        except ValueError:
            print("Error: Year must be a number.")
    else:
        print("Usage: python aoc_utils/file_creation.py <YEAR>")