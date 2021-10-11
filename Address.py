a = [1,2,3,4,5]
# b = a[0:4:1]
# b = a
b = [*a]
print(hex(id(a)))
print(hex(id(b)))
# cann't use int to convert it to hex
# id gives addr in base 10

a = {
  'name': 'Jack',
  'age': 10
}
# b = a
b = {**a}
print(hex(id(a)))
print(hex(id(b)))

