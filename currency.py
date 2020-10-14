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
    # print(count)
    assert count > 0, 'PRECONDITION: Need at least one space in string.'
    # s = introcs.lstrip(s)
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
    s = s[spaceIndex + 1:]
    # s = introcs.strip(s)
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
    count = introcs.count_str(s, "\"")
    assert count >= 2;
    firstQuoteIndex = introcs.find_str(s, "\"")
    s = s[firstQuoteIndex + 1:]
    lastQuoteIndex = introcs.find_str(s, "\"")
    s = s[:lastQuoteIndex]
    return s


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    On the other hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    findSrc = introcs.find_str(json, ',')
    json = json[findSrc+1:]
    findSrc = introcs.find_str(json, ':')
    json = json[findSrc:]
    #print(src)
    return first_inside_quotes(json)


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'


    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    findDST = introcs.find_str(json, ',')
    json = json[findDST + 1:]
    findDST = introcs.find_str(json, ',')
    json = json[findDST + 1:]
    FindDST = introcs.find_str(json, ':')
    json = json[FindDST + 1:]

    #print(first_inside_quotes(json))
    return first_inside_quotes(json)


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message
    'Source currency code is invalid'). On the other hand if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    findError = introcs.rfind_str(json, ':')
    json = json[findError:]
    print(json)
    count = introcs.isprintable(first_inside_quotes(json))
    print(count)
    #return


has_error('{"success": false, "src": "", "dst": "", "error": "The rate for currency EUF is not present."}')
