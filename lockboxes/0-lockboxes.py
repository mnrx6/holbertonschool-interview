#!/usr/bin/python3
"""Lockboxes module."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened."""
    opened = {0}
    to_visit = [0]

    while len(to_visit) > 0:
        current_box = to_visit.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                to_visit.append(key)

    if len(opened) == len(boxes):
        return True
    else:
        return False
