import re
from collections import Counter

# Regular expression for matching URLs in Apache access logs
URL_PATTERN = r'"(GET|POST|HEAD|PUT|DELETE) (.*?) HTTP'

# Open the log file and read its contents
with open('/path/to/access.log', 'r') as f:
    log_data = f.read()

# Use regular expressions to extract the URLs from the log file
urls = re.findall(URL_PATTERN, log_data)

# Initialize a Counter object to count the number of occurrences of each URL
url_counts = Counter([url[1] for url in urls])

# Print out the top 10 most requested URLs
print('Top 10 Most Requested URLs:')
for url, count in url_counts.most_common(10):
    print(f'{count} requests - {url}')