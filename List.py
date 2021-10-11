from list import List

mylist = List(1,2,3,4)
print(mylist.get(1))
mylist.set(2, 10)
print(mylist.get(2))
print(mylist.get(-1))

print(mylist)
print(mylist.length())

# Copying List
cart = ['notbook', 'pencil']

# Copying
newCartByDefault = cart[:]
newCartBySpread = [*cart]

print(hex(id(cart)))
print(hex(id(newCartByDefault)))
print(hex(id(newCartBySpread)))

# This is to be avoided
newCardByPointer = cart
print(hex(id(newCardByPointer)))
