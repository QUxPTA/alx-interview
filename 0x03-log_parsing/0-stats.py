#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys
import signal
import re
from collections import defaultdict

# Regular expression pattern for log entry
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>[^\]]+)\] "GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)'
)

# Dictionary to count status codes
status_counts = defaultdict(int)
# Variable to accumulate total file size
total_size = 0
# Counter for lines read
line_count = 0

# List of valid status codes
valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}


def signal_handler(sig, frame):
    """
    Signal handler for keyboard interruption (CTRL + C).
    Prints the summary of the log metrics and exits the program.

    Args:
        sig: Signal number.
        frame: Current stack frame.
    """
    print_summary()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def process_log_entry(log_entry):
    """
    Process a single log entry.
    Validates and parses the log entry, updates the total file size, and counts status codes.
    Prints a summary every 10 lines.

    Args:
        log_entry (str): A single log entry.
    """
    global total_size, line_count
    match = log_pattern.match(log_entry)
    if match:
        status = match.group('status')
        size = int(match.group('size'))
        total_size += size
        if status in valid_status_codes:
            status_counts[status] += 1
        line_count += 1

        # Print summary every 10 lines
        if line_count % 10 == 0:
            print_summary()


def print_summary():
    """
    Print the summary of the log metrics.
    Includes total file size and the count of each status code in ascending order.
    """
    print(f"Fcile size: {total_size}")
    for status in sorted(status_counts.keys()):
        print(f"{status}: {status_counts[status]}")


def main():
    """
    Main function to read and process log entries from standard input.
    Processes each line of input and prints a final summary when done.
    """
    for line in sys.stdin:
        process_log_entry(line.strip())
    # Print final summary if script ends naturally
    print_summary()


if __name__ == "__main__":
    main()
