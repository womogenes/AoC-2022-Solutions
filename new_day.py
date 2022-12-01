# Generate a new day with all files and stuff
import os

import datetime as dt
day = (dt.datetime.now() + dt.timedelta(days=1, hours=4, minutes=30)).day

prefix = f"day_{str(day).zfill(2)}"

if not prefix in os.listdir():
    os.mkdir(prefix)
    os.chdir(prefix)
    with open(f"./{prefix}_p1.py", "w") as fout:
        fout.write(f"""# from aocd import lines, submit


# submit(ans)
""")

    open(f"./{prefix}_p2.py", "w")
    open(f"./{prefix}_sample.in", "w")
