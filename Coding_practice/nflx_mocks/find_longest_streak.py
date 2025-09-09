# This is a mock from perplexity
# <!-- Here is a **mock Netflix Data Engineering coding interview question**, modeled closely on recent screens:

# ***

# ### Netflix Coding Mock Interview Question

# **Prompt:**

# Netflix streams shows to millions of users worldwide. Each user's viewing activity is logged in a log table as:

# ```text
# user_id | session_id | timestamp        | show_id
# --------|------------|------------------|--------
# U1      | S1         | 2025-08-15 18:04 | SH101
# U1      | S2         | 2025-08-16 19:05 | SH101
# U2      | S7         | 2025-08-15 21:22 | SH201
# ...     | ...        | ...              | ...
# ```

# Users often watch daily, but sometimes logs are missing or duplicated (idempotency issues).

# **Task:**

# Write a Python function to find, for each user, the length of their **longest daily viewing streak** (number of consecutive days with at least one session).

# - Assume the logs are unsorted and may contain duplicate (user_id, session_id, timestamp, show_id) rows.
# - Return a dictionary: `{user_id: max_streak_length}`.

# ***

# #### Example Input

# ```python
# logs = [
#     ("U1", "S1", "2025-08-15 18:04", "SH101"),
#     ("U1", "S2", "2025-08-16 19:05", "SH101"),
#     ("U1", "S3", "2025-08-16 19:06", "SH102"),
#     ("U2", "S7", "2025-08-15 21:22", "SH201"),
#     ("U1", "S4", "2025-08-17 21:10", "SH105"),
#     ("U2", "S8", "2025-08-18 10:20", "SH101"),
#     ("U2", "S8", "2025-08-18 10:20", "SH101"),  # duplicate
# ]
# ```

# #### Example Output

# ```python
# # U1: 2025-08-15, 2025-08-16, 2025-08-17 = 3 days streak
# # U2: 2025-08-15, 2025-08-18 = 1-day streaks (non-consecutive)
# {"U1": 3, "U2": 1}
# ```

# *** -->

from collections import defaultdict
from datetime import datetime

def find_longest_streak(sessions):
    views = defaultdict(set)
    for user,session,time,show in sessions:
        dt = time.split(" ")[0]
        views[user].add(dt)
    
    streaks = {}
    for user,dts in views.items():
        dts = [datetime.strptime(x,'%Y-%m-%d').date() for x in dts]
        sorted_dts = sorted(dts)
        current_streak = 1
        max_streak = 1
        #print(sorted_dts)
        for i in range(1,len(sorted_dts)):
            if (sorted_dts[i]-sorted_dts[i-1]).days==1:
                current_streak += 1
                max_streak = max(max_streak,current_streak)
            else:
                current_streak = 1
        streaks[user]=max_streak
    return streaks


logs = [
    ("U1", "S1", "2025-08-15 18:04", "SH101"),
    ("U1", "S2", "2025-08-16 19:05", "SH101"),
    ("U1", "S3", "2025-08-16 19:06", "SH102"),
    ("U2", "S7", "2025-08-15 21:22", "SH201"),
    ("U1", "S4", "2025-08-17 21:10", "SH105"),
    ("U2", "S8", "2025-08-18 10:20", "SH101"),
    ("U2", "S8", "2025-08-18 10:20", "SH101")
]

assert find_longest_streak(logs) ==  {'U1': 3, 'U2': 1}