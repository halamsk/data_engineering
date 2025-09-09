# # Perplexity
# Here’s another **Netflix-style data engineering coding question** based on real interviews and recent screens:

# ***

# ### Netflix Coding Mock Interview Question 2

# **Prompt:**

# Netflix wants to monitor the performance and reliability of its video streaming service. Each time a user watches a show, the system records a log entry:

# ```text
# user_id | session_id | timestamp        | status_code
# --------|------------|------------------|-------------
# U1      | S1         | 2025-09-06 19:30 | 200
# U1      | S2         | 2025-09-06 20:01 | 500
# U2      | S4         | 2025-09-06 20:34 | 404
# U1      | S5         | 2025-09-07 18:12 | 200
# ...     | ...        | ...              | ...
# ```

# Each session may have a status code (200 = success, others = failure).

# **Task:**

# Write a Python function to compute the following, for each user:
# - The date of their **first failed session (status code ≠ 200)**.
# - The **percentage of failed sessions** out of their total sessions.

# Return a dictionary with the following structure, for each user:
# ```python
# {"U1": ("2025-09-06", 33.33), ...}
# ```
# (Date string in "YYYY-MM-DD" format, percentage as a float rounded to 2 decimal points.)

# ***

# #### Example Input

# ```python
# logs = [
#     ("U1", "S1", "2025-09-06 19:30", 200),
#     ("U1", "S2", "2025-09-06 20:01", 500),
#     ("U2", "S4", "2025-09-06 20:34", 404),
#     ("U1", "S5", "2025-09-07 18:12", 200),
#     ("U2", "S6", "2025-09-06 21:00", 200)
# ]
# ```

# #### Example Output

# ```python
# {
#  "U1": ("2025-09-06", 33.33), # 1 failure out of 3 sessions (S2 is first fail)
#  "U2": ("2025-09-06", 50.0),  # 1 failure (404) out of 2 sessions (S4 first fail)
# }
# ```

# ***
from datetime import datetime

def find_failed_session_rate(sessions):
    agg_dict={}
    for user,session,dtime,status in sessions:
        dt = dtime.split()[0]
        dt = datetime.strptime(dt, '%Y-%m-%d').date()
        failure_count = 1 if status!=200 else 0
        print(f"failure_count={failure_count}, status={status}")
        failure_date =  dt if status!="200" else "9999-12-31"
        if user not in agg_dict:
           agg_dict[user]={"total_sessions":1, "failure": failure_count, "fail_date": failure_date}
        else:
           agg_dict[user]["total_sessions"] += 1
           agg_dict[user]["failure"] += failure_count
           agg_dict[user]["fail_date"] = min(failure_date,agg_dict[user]["fail_date"])

    result = {}
    print(agg_dict)
    for k,v in agg_dict.items():
        result[k]=(str(v["fail_date"]),round((v["failure"]/v["total_sessions"])*100,2))
    return result             


logs = [
    ("U1", "S1", "2025-09-06 19:30", 200),
    ("U1", "S2", "2025-09-06 20:01", 500),
    ("U2", "S4", "2025-09-06 20:34", 404),
    ("U1", "S5", "2025-09-07 18:12", 200),
    ("U2", "S6", "2025-09-06 21:00", 200)
]

assert(find_failed_session_rate(logs)) == {
 "U1": ("2025-09-06", 33.33), # 1 failure out of 3 sessions (S2 is first fail)
 "U2": ("2025-09-06", 50.0),  # 1 failure (404) out of 2 sessions (S4 first fail)
}
print("success")