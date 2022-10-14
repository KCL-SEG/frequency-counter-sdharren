"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        item = str(item)
        frequencies[item] = frequencies.get(item, 0) + 1
    return frequencies
