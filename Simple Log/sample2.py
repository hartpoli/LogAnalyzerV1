import re

# Regular expression for matching IP addresses in Apache access logs
IP_PATTERN = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# Open the log file and read its contents
with open('/path/to/access.log', 'r') as f:
    log_data = f.read()

# Split the log file into individual log entries
log_entries = log_data.split('\n')

# Initialize a dictionary to store the number of requests per IP address
ip_counts = {}

# Loop through each log entry and count the number of requests per IP address
for entry in log_entries:
    # Use regular expressions to extract the IP address from the log entry
    match = re.search(IP_PATTERN, entry)
    if match:
        ip = match.group(0)
        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1

# Print the results
for ip, count in ip_counts.items():
    print(f'{ip}: {count}')