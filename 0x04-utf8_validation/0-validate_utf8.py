#!/usr/bin/env python3
"""leetcode solution for utf-8 validation"""


def validUTF8(data):
    """validates data to be in utf-8"""
    number_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6
    for byte in data:
        mask = 1 << 7
        if number_bytes == 0:
            while mask & byte:
                number_bytes += 1
                mask = mask >> 1

            if number_bytes == 0:
                continue
            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            if not(byte & mask1 and not (byte & mask2)):
                return False
        number_bytes -= 1
    return number_bytes == 0
