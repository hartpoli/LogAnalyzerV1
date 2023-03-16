import re

# Regular expression for matching request times in Apache access logs
TIME_PATTERN = r'\d+\.\d+'

# Open the log file and read its contents
with open('/path/to/access.log', 'r') as f:
    log_data = f.read()

# Split the log file into individual log entries
log_entries = log_data.split('\n')

# Initialize a list to store the response times for each request
response_times = []

# Loop through each log entry and extract the request time
for entry in log_entries:
    # Use regular expressions to extract the request time from the log entry
    match = re.search(TIME_PATTERN, entry)
    if match:
        time = float(match.group(0))
        response_times.append(time)

# Calculate the average response time and print it out
if len(response_times) > 0:
    avg_time = sum(response_times) / len(response_times)
    print(f'Average response time: {avg_time:.3f} seconds')
else:
    print('No requests found in log file')