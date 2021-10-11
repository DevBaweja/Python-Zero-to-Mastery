# import string
from string import String

first = 'dev'
last = 'baweja'


# mystring = string('Hi I am {}')
# mystring.format(first)
# print(mystring)

# mystr = string.String('Hi I am {}')
mystr = String('Hi I am {}')

# Functional Chaining
mystr.format(first).format(last)


print(mystr)

# print(string('Hi I am {}').format(first))

# from math import gcd,floor
 