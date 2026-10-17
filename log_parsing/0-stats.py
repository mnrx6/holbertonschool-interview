#!/usr/bin/python3
"""Log parsing script"""

import sys

t_size = 0
count = 0
status = {}


def print_stats():
    """Print file size and status codes"""
    print("File size: {}".format(t_size))

    for code in sorted(status):
        print("{}: {}".format(code, status[code]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()

            if len(parts) >= 2:
                try:
                    status_code = int(parts[-2])
                    file_size = int(parts[-1])
                    t_size += file_size

                    if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                        if status_code in status:
                            status[status_code] += 1
                        else:
                            status[status_code] = 1

                except ValueError:
                    pass

            if count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        pass

    finally:
        if count == 0 or count % 10 != 0:
            print_stats()
