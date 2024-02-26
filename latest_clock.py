"""
Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.

The time should be in HH:MM format.

Examples:

digits: 1, 9, 8, 3 => result: "19:38"
digits: 9, 1, 2, 5 => result: "21:59" ("19:25" is also a valid time, but 21:59 is later)
Notes
Result should be a valid 24-hour time, between 00:00 and 23:59.
Only inputs which have valid answers are tested.
"""

from datetime import time
from itertools import permutations

def latest_clock(a, b, c, d):

    permutations_list = list(permutations([a,b,c,d]))
    valid_times = set()

    for combo in permutations_list:
        try:
            constructed_time = time(int('{}{}'.format(int(combo[0]), int(combo[1]))), int('{}{}'.format(int(combo[2]), int(combo[3]))))
    
        except ValueError:
            pass

        else:
            valid_times.add(constructed_time)

    latest = max(valid_times)

    return str(latest)[:5]
