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
    introcs.assert_equals('B C', result, 'Did not meet testing qualifications.')
    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result, 'Did not meet testing qualifications.')
    result = currency.first_inside_quotes('"A B"')
    introcs.assert_equals('A B', result, 'Did not meet testing qualifications.')
    result = currency.first_inside_quotes('A B""""""""')
    introcs.assert_equals('', result, 'Did not meet testing qualifications.')


def test_get_src():
    """Test procedure for get_src"""
    print('Testing get_src')
    result = currency.get_src(
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error":''""}')
    introcs.assert_equals('2 United States Dollars', result, 'Did not meet test requirements.')
    result = currency.get_src('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars', result, 'Did not meet test requirements.')
    result = currency.get_src('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals("", result, 'Did not meet test requirements.')
    result = currency.get_src('{"success": true,"src": "","dst": "","error": "Source currency code is invalid."}')
    introcs.assert_equals("", result, 'Did not meet test requirements.')
    result = currency.get_src('{"success": false, "src": "", "dst": "", "error": "The rate for currency EUF is not present."}')
    introcs.assert_equals('', result, 'Did not meet test requirements')

def test_get_dst():
    """Test procedure for get_dst"""
    print('Testing get_dst')
    result = currency.get_dst('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result, 'Did not meet test requirements.')
    result = currency.get_dst('{"success":true,"src":"2 United States Dollars","dst":"1.772814 Euros","error":""}')
    introcs.assert_equals('1.772814 Euros', result, 'Did not meet test requirements.')
    result = currency.get_dst('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals("", result, 'Did not meet test requirements.')
    result = currency.get_dst('{"success": true,"src": "","dst": "","error": "Source currency code is invalid."}')
    introcs.assert_equals("", result, 'Did not meet test requirements.')
    result = currency.get_dst('{"success": false, "src": "", "dst": "", "error": "The rate for currency EUF is not present."}')
    introcs.assert_equals('', result, 'Did not meet test requirements')

def test_has_error():
    """Test procedure for has_error"""
    print('Testing has_error')
    result = currency.has_error(
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(result, 'Did not meet test requirements.')
    result = currency.has_error('{"success":true,"src":"2 United States Dollars","dst":"1.772814 Euros","error":""}')
    introcs.assert_false(result, 'Did not meet test requirements.')
    result = currency.has_error('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_true(result, 'Did not meet test requirements.')
    result = currency.has_error('{"success": true,"src": "","dst": "","error": "Source currency code is invalid."}')
    introcs.assert_true(result, 'Did not meet test requirements.')



def test_service_response():
    """Test procedure for service_response"""
    print('Testing service_response')
    result = currency.service_response('USD','EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars", "dst": "2.2160175 Euros", "error": ""}', result)
    result = currency.service_response('USSD','EUR',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The rate for currency USSD is not present."}',result)
    result = currency.service_response('USD','MEX',20)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The rate for currency MEX is not present."}', result)
    result = currency.service_response('USD','USD',-2.5)
    introcs.assert_equals('{"success": true, "src": "-2.5 United States Dollars", "dst": "-2.5 United States Dollars", "error": ""}', result)

def test_iscurrency():
    """Test procedurae for iscurrency"""
    print('Testing iscurrency')
    result = currency.iscurrency('ABC')
    introcs.assert_false(result)
    result = currency.iscurrency('USD')
    introcs.assert_true(result)
    result = currency.iscurrency('JPY',)
    introcs.assert_true(result)

def test_exchange():
    """Test procedure for exchange"""
    print('Testing exchange')
    result = currency.exchange('USD', 'EUR', 2.5)
    introcs.assert_equals('2.5', result)
    result = currency.service_response('USSD', 'EUR', 2.5)
    introcs.assert_equals('',result, 'Did not meet test requirements.')


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
