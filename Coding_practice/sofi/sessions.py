# logs are like [(1,100001),(1,100005),(2,10001)] etc .. first column is user and second 
# is timestamp of events .. the logs are not sorted, 
# if the timestamp between 2 events are not over 5 mins then its same session else new session , 
# please write python code to provide like 
# user_id,session_id(u1_s1), session start, session end, total session mins .. timestamp is in epco

from collections import defaultdict
import datetime

logs = [(1, 100001), (1, 100005), (2, 10001), (1, 10300), (2, 10550), (2, 11000)]

# Step 1: Group logs by user
user_logs = defaultdict(list)
for user_id, timestamp in logs:
    user_logs[user_id].append(timestamp)

# Step 2–4: Process each user's logs to form sessions
output = []
for user_id, timestamps in user_logs.items():
    timestamps.sort()
    session_num = 1
    session_start = timestamps[0]
    session_end = timestamps[0]
    
    for i in range(1, len(timestamps)):
        if timestamps[i] - session_end > 300:
            # Save previous session
            session_id = f"u{user_id}_s{session_num}"
            session_minutes = (session_end - session_start) / 60
            output.append((user_id, session_id, session_start, session_end, round(session_minutes, 2)))
            # Start new session
            session_num += 1
            session_start = timestamps[i]
        
        session_end = timestamps[i]
    
    # Save the last session
    session_id = f"u{user_id}_s{session_num}"
    session_minutes = (session_end - session_start) / 60
    output.append((user_id, session_id, session_start, session_end, round(session_minutes, 2)))

# Display results
for row in output:
    print(f"user_id: {row[0]}, session_id: {row[1]}, session_start: {row[2]}, session_end: {row[3]}, session_minutes: {row[4]}")