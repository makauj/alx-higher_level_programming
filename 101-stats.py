#!/usr/bin/python3
"""script thst reads stdin line by line and computes metrics"""
import sys


def print_stats(total_size, status_codes):
    """prints total file size and status code metrics"""
    print(f"filesize: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        try:
            total_size += int(parts[-1])
            status_code = int(parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (IndexError, ValueError):
            pass

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    pass

finally:
    print_stats(total_size, status_codes)