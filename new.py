"""Usage: python new.py <topic> <level> <problem_name>
Example: python new.py hashing easy two_sum
"""
import sys
from datetime import date
from pathlib import Path

if len(sys.argv) != 4:
    sys.exit(__doc__)

topic, level, name = sys.argv[1:]
matches = list(Path(".").glob(f"*_{topic}"))
if not matches:
    sys.exit(f"Topic folder '{topic}' nahi mila")

target = matches[0] / level / f"{name}.py"
if target.exists():
    sys.exit(f"{target} pehle se hai")

template = Path("templates/solution_template.py").read_text(encoding="utf-8")
target.write_text(template.replace("{DATE}", str(date.today())), encoding="utf-8")
print(f"Created: {target}")