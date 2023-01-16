#!/bin/usr/python3
"""This is a peak function"""

def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]

