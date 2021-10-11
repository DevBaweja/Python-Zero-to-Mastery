if False:
  pass
elif False:
  pass
else:
  pass

# and or

# Truthy Falsy
None
False
0
0.0
0j
[]
{}
set()
()
''

# Ternary Operator
'True' if True else 'False'

# Short Circuiting

'True' or 'Circuit'
'False' and 'Circuit'

# Logical Operators

# <=, >=, <, >, ==, !=
# and or not
1<2<3<4

# == vs is
# == will convert into same type
# is will check type and memory

# Loops
for item in 'Zero':
  pass

# Iterable
# list, dictionary, set, tuple, string, range
# Iterate


# object.items(), object.keys(), object.values()
# for key,value in object.items():
   
# Range
# list(range(value))  

# for _ in range(start, end, step):

# Enumerate
# for index,value in enumerate(iterable)

# While
while True:
  pass
  break
else:
  pass 
# Else only execute with no break
# break, continue, pass

# clean, readability, predictability, DRY(Do not repeat), reusable

# if value in list:
# if value not in list:

# Arguments and Parameters
# Positional Arguments
# Keyword Arguments 

# Default Parameters

# Closure

def sum(a,b):
  def inner_sum():
    return a+b
  return inner_sum

sum(1,1)()

# DocsString
def test():
  '''
  This test the value
  '''
  print('test');

help(test)
# test.__doc__

# *args, **kwargs
# Rest Operator
def sum(*args,**kwargs):
  print(args)
  print(kwargs)

sum(0,0,a=0,b=0)

# params, *args, default params, **kwargs

# Scope
# local, prototype, global, build in

total = 0
def count():
  global total
  total += 1
  return total

count()
count()

total = 0
def count(total):
  total += 1
  return total

count(total)
count(total)

# global
# nonlocal

def outer():
  x = 'local'
  def inner():
    nonlocal x
    x = 'nonlocal'
    print(x)
  
  inner()
  print(x)

outer()