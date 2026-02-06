"""
The purpose of this module is to provide a simple interface for importing data from files.
It automatically resolves paths based on the calling script's location.
"""

import inspect
import aocd
import re
from pathlib import Path

def _get_caller_context():
    """
    Internal helper to determine the path of the script calling this module.
    Returns: (folder_path, filename_stem)
             e.g. (/home/ryan/repos/aoc/2015, "day08")
    """
    # 1. Get the stack frame of the caller (2 frames up: this helper -> public func -> caller)
    # We iterate up the stack to find the first file that isn't THIS file.
    stack = inspect.stack()
    this_file = Path(__file__).resolve()
    
    for frame in stack:
        caller_path = Path(frame.filename).resolve()
        if caller_path != this_file:
            return caller_path.parent, caller_path.stem
    
    raise RuntimeError("Could not determine caller context.")

def _infer_day_year(folder_path, filename_stem):
    """
    Attempts to guess the Day and Year from the folder structure and filename.
    Expects structure: .../2015/day08.py
    """
    # Infer Day from filename (e.g., "day08" -> 8)
    day_match = re.search(r'\d+', filename_stem)
    day = int(day_match.group()) if day_match else None

    # Infer Year from folder name (e.g., "2015" -> 2015)
    # Checks current folder, then parent folder
    year = None
    if re.match(r'^\d{4}$', folder_path.name):
        year = int(folder_path.name)
    elif re.match(r'^\d{4}$', folder_path.parent.name):
        year = int(folder_path.parent.name)

    return day, year

def get_input(filename=None):
    """
    Automatically finds the input file for the calling script.
    If the file does not exist, it attempts to download it using aocd.
    
    Args:
        filename (str, optional): Override the auto-detected filename (e.g. "test.txt")
    """
    folder_path, stem = _get_caller_context()
    
    # Define the input directory relative to the caller
    input_dir = folder_path / "input"
    input_dir.mkdir(parents=True, exist_ok=True) # Ensure folder exists

    # Determine target filename
    if filename:
        target_file = input_dir / filename
    else:
        # Default: "day08.py" -> "day08.txt"
        target_file = input_dir / f"{stem}.txt"

    # Auto-Download if missing and we are looking for the standard input
    if not target_file.exists() and filename is None:
        print(f"Input file not found at {target_file}. Attempting auto-download...")
        day, year = _infer_day_year(folder_path, stem)
        
        if day and year:
            download(day, year) # Reuse our download function
        else:
            print("Could not infer Day/Year for auto-download.")

    if target_file.exists():
        return target_file.read_text().strip()
    else:
        raise FileNotFoundError(f"Could not find input file: {target_file}")

def download(day, year=None):
    """
    Downloads data from AoC and saves it to the caller's input folder.
    """
    folder_path, _ = _get_caller_context()
    
    # If year isn't provided, try to guess it from the folder name
    if year is None and folder_path.name.isdigit():
        year = int(folder_path.name)

    print(f"Downloading data for Day {day}, Year {year}...")
    data = aocd.get_data(day=day, year=year)
    
    # Format filename: 8 -> "day08.txt"
    filename = f"day{day:02}.txt"
    input_dir = folder_path / "input"
    input_dir.mkdir(parents=True, exist_ok=True)
    
    save_path = input_dir / filename
    save_path.write_text(data)
    print(f"Saved to {save_path}")

def preview(lines=5):
    """
    Prints the first few lines of the auto-detected input file.
    """
    data = get_input()
    print(f"--- Input Preview ({lines} lines) ---")
    for line in data.splitlines()[:lines]:
        print(line)
    print("-------------------------------------")

if __name__ == "__main__":
    # Test block
    print("This module is intended to be imported, not run directly.")