# Spread Operators
# Rest Operators
# Default Parameters
# Object/Array Destructing

obj = {
  'name': 'dev',
  'age': 10
}

newObj = { **obj }
newObj ={ **obj, 'name': 'jai', 'key': 'value' }
print(newObj)

o = [*obj]
print(o) 

arr = ['dev',12]

newArr = [ *arr ]
print(newArr)

name = 'dev'

# string = f'I am {name}'
string = 'I am {}'.format(name)
print(string)

# Functional Chaining
print({
  'name': 'dev'
}['name'].upper().isupper())
print(['dev','baweja'][0])

a = [0,1,2,3]
# print(len(a))

a = 'ewfvrever'
# print(len(a))

a  = {
  'key': 'value',
  'name': 'dev'
}
# print(len(a))
# print(a['key'],a['name'])
# print(*a)
b = [*a]
b = {**a}

# print(b)

# loop
# key value

# obj
# [*obj]
# key obj[key]
for arr in ['dev','baweja']:
  print(arr)
for key in [*a]:
  print(f'{key}: {a[key]}')

for key in a:
  print(key,a[key])

