multi = '''

''';


first = 'dev'
last = 'baweja'
# print('My name is '+ first +' '+ last);

# Access var in str literal
# print(''' My name is ''')

# Literal Synatx
# a = list()
# b = dict()
# a = []
# b = {}

# String Literal / Formatted Sting
print(f'My name is {first} {last}')

first = 'dev'
last = 'baweja'
age = 20
# str concatenation 
print('My name is '+first+' '+last+'. I am '+str(age)+' years old.')
# String Literal
print(f'My name is {first} {last}. I am {age} years old.')
# format Syntax

string = str('My name is {} {}. I am {} years old.')
mystr = string.format(first, last, age)
