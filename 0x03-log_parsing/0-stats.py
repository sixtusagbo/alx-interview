#!/usr/bin/python3
"""Log parser"""
import sys
from typing import List
import re


def is_skippable(line: List[str]) -> bool:
    """Check whether a line is skippable"""
    if len(line) != 9:
        return False

    ip_address = line[0]
    # Validate IP Address
    if not re.match(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", ip_address):
        return False

    # Validate date
    date = " ".join([line[2][1:], line[3][:-1]])
    if not re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}", date):
        return False

    endpoint = " ".join([line[4], line[5], line[6]])
    # Validate endpoint
    if endpoint != '"GET /projects/260 HTTP/1.1"':
        return False

    # Validate file size
    file_size = line[8]
    if not isinstance(file_size, int):
        return False

    return True


def parse_lines(lines: List[str]):
    """Parse some lines from stdin"""
    if not lines:
        return
    file_size = 0
    status_codes_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    for log in lines:
        line = log.split(" ")
        if is_skippable(line):
            continue
        file_size += int(line[8])
        try:
            status_code = int(line[7])
        except ValueError:
            status_code = None
        if status_code and status_code in status_codes_count.keys():
            status_codes_count[status_code] += 1
    print("File size: {}".format(file_size))
    for key, value in status_codes_count.items():
        if value != 0:
            print("{}: {}".format(key, value))


def extract_lines():
    """Read a given number of lines from standard input"""
    lines = []
    try:
        count = 1
        while True:
            line = sys.stdin.readline().rstrip()
            if not line.strip():
                continue
            lines.append(line)
            if count == 10:
                parse_lines(lines)
                count = 0
            count += 1
    except KeyboardInterrupt:
        parse_lines(lines)


if __name__ == "__main__":
    extract_lines()