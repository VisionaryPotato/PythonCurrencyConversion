"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Sergio Olvera
Date:   10/10/2020
"""

import introcs
import currency

def test_before_space():
    """Test procedure for before_space"""
    print('Testing before_space')
    result = currency.before_space("hello world")
    introcs.assert_equals('hello', result, 'Did not meet testing qualifications')
    result = currency.before_space('Bob Andrew    ')
    introcs.assert_equals('Bob', result, 'Did not meet testing qualifications')
    result = currency.before_space('Bob  Andrew')
    introcs.assert_equals('Bob', result, 'Did not meet testing qualifications')
    result = currency.before_space(' ')
    introcs.assert_equals('', result, 'Did not meet testing qualifications')
    result = currency.before_space('hello ')
    introcs.assert_equals('hello', result, 'Did not meet testing qualifications')
    result = currency.before_space(' hello')
    introcs.assert_equals('', result, 'Did not meet testing qualifications')

def test_after_space():
    """Test procedure for after_space"""
    print('Testing after_space')
    result = currency.after_space("hello world")
    introcs.assert_equals('world', result, 'Did not meet testing qualifications')
    result = currency.after_space(' ')
    introcs.assert_equals('', result, 'Did not meet testing qualifications')
    result = currency.after_space(' hello')
    introcs.assert_equals('hello', result, 'Did not meet testing qualifications')
    result = currency.after_space('hello  ')
    introcs.assert_equals(' ', result, 'Did not meet testing qualifications')
    result = currency.after_space('Bob Andrew ')
    introcs.assert_equals('Andrew ', result, 'Did not meet testing qualifications')
def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print('Testing first_inside_quotes')
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result,'Did not meet testing qualifications')
    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result,'Did not meet testing qualifications')


def test_get_src():
    """Test procedure for get_src"""
    print('Testing get_src')


def test_get_dst():
    """Test procedure for get_dst"""
    print('Testing get_dst')


def test_has_error():
    """Test procedure for has_error"""
    print('Testing has_error')


def test_service_response():
    """Test procedure for service_response"""
    print('Testing service_response')


def test_iscurrency():
    """Test procedure for iscurrency"""
    print('Testing iscurrency')


def test_exchange():
    """Test procedure for exchange"""
    print('Testing exchange')


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print('All tests completed successfully')