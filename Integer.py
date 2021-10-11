# Default Parameters
def integer(s,base=10):
  if type(s) == float or type(s) == int:
    return int(s)
  return int(s,base)

print(integer(2.1))

print(integer('241'))
# print(integer('53E'))
print(integer('53E',16))
print(integer('213E',16))

print(integer('10100111110',2))
print(integer('1324',10))



