a = 'cre gDSVv dvCev'
# print(a.swapcase())

def swap(a):
  new = ''
  for char in list(a):
    newchar = char 
    if(char.isupper()):
      newchar = char.lower()
    if(char.islower()):
      newchar = char.upper()
    if(char == ' '):
      newchar = ' '
    new += newchar
  return new

print(swap(a))