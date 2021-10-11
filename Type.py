print(type(type))
# <class 'type'>
print(type(int))
# <class 'type'>

print(type(int()))
# <class 'int'>

print(type([]))
# <class 'list'>
print(type({}))
# <class 'dict'>
print(type(()))
# <class 'tuple'>
print(type(set()))
# <class 'set'>

def fn():
  print('fn')

print(type(fn))
# <class 'function'>
print(type(fn()))
# <class 'NoneType'>
print(type(None))
# <class 'NoneType'>

def r():
  return '';

print(type(r()))
# <class 'str'>

print(type(4/2))
print(type(int(4/2)))

def fn():
  pass
print(fn)
# <function fn at 0x7fe3d418f3a0>

print(type(fn))
# <class 'function'>

print(round)
# <built-in function round>
print(round)
# <class 'buildin_function_or_method'>



