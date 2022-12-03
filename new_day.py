# Generate a new day with all files and stuff
import os

import datetime as dt
day = (dt.datetime.now() + dt.timedelta(hours=4, minutes=30)).day
year = dt.datetime.now().year

prefix = f"day_{str(day).zfill(2)}"

if not prefix in os.listdir():
    os.mkdir(prefix)
    os.chdir(prefix)
    with open(f"./{prefix}_p1.py", "w") as fout:
        fout.write(f"""# from aocd import submit
from pyperclip import copy


# submit(ans, part="a", day={day}, year={year})
""")

    with open(f"./{prefix}_p2.py", "w") as fout:
        fout.write(f"""# from aocd import submit
from pyperclip import copy


# submit(ans, part="b", day={day}, year={year})
""")

    open(f"./{prefix}_sample.in", "w")
