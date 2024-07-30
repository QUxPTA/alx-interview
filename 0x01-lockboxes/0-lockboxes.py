#!/usr/bin/python3
"""
A function to determine if all boxes can be opened
given a list of lists representing the boxes and their keys.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): A list where each element is a list
                                     containing the keys in a particular box.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    n = len(boxes)
    opened_boxes = set([0])  # Start with the first box opened
    keys = list(boxes[0])  # Start with keys from the first box

    while keys:
        key = keys.pop()
        if key < n and key not in opened_boxes:
            opened_boxes.add(key)
            keys.extend(boxes[key])

    return len(opened_boxes) == n
