"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Sergio Olvera
Date:   10/10/2020
"""
import currency
SRC = input('3-letter code for original currency: ')
DST = input('3-letter code for the new currency: ')
AMT = float(input('Amount of the original currency: '))
dst = float(currency.exchange(SRC,DST,AMT))
dst = round(dst, 3)
EXCHANGE = print('You can exchange '+str(AMT)+' '+ SRC + ' for ' +str(dst) + ' ' + DST +'.')