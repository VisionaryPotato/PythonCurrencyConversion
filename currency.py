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
    count = introcs.count_str(s, ' ')
    #print(count)
    assert count > 0, 'PRECONDITION: Need at least one space in string.'
    #s = introcs.lstrip(s)
    spaceIndex = introcs.find_str(s, ' ')
    s = s[:spaceIndex]
    return s


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    count = introcs.count_str(s, ' ')
    assert count > 0, 'PRECONDITION: Need at least one space in string.'
    spaceIndex = introcs.find_str(s, ' ')
    s = s[spaceIndex+1:]
    #s = introcs.strip(s)
    return s


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    pass
