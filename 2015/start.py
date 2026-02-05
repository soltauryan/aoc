import sys
import os
from datetime import date

day = int(sys.argv[1]) if len(sys.argv) > 1 else date.today().day
year = int(sys.argv[2]) if len(sys.argv) > 2 else date.today().year

filename = f"day{day:02d}.py"
if os.path.exists(filename):
    print(f"{filename} already exists")
    sys.exit(1)
    
template = f"""import aocd
import utils

lines = aocd.get_data(day={day}, year={year})
data = lines.splitlines()

def part1(lines):
    pass
    
def part2(lines):
    pass
    
if __name__== "__main__":
    pass
"""

with open(filename, 'w') as f:
    f.write(template)

print(f"Created {filename}")