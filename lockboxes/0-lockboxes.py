#!/usr/bin/python3
"""Determine whether every box in a set of lockboxes can be opened."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, starting from box 0.

    Each box may hold keys to other boxes. A key opens the box with
    the same number. Keys with no matching box are ignored.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    opened = {0}
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if isinstance(key, int) and 0 <= key < n and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == n
