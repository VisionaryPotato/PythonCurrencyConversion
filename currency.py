"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Sergio Olvera
Date:   10/10/2020
"""
import introcs

APIKEY = 'H2u53AGBwvuiofitARa0lKQgnnkNThgrV8hn3XGxYT0e'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    newVal = introcs.strip(s)
    spaceIndex = introcs.find_str(newVal, ' ')
    newString = newVal[:spaceIndex]
    return newString