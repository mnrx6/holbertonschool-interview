#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Check if data is valid UTF-8."""
    num_of_bytes = 0

    for num in data:
        num = num & 255
        if num_of_bytes == 0:
            if (num >> 7) == 0:
                continue
            elif (num >> 5) == 6:
                num_of_bytes = 1
            elif (num >> 4) == 14:
                num_of_bytes = 2
            elif (num >> 3) == 30:
                num_of_bytes = 3
            else:
                return False
        else:
            if (num >> 6) == 2:
                num_of_bytes -= 1
            else:
                return False
    if num_of_bytes == 0:
        return True
    else:
        return False
