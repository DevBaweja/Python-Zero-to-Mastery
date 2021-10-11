print(round)
# <build-in function round>

# round(number, ndigits)
print(round(12.14))
# 12
print(round(2.135,2))
# 2.13 
print(round(2.1,0))
# 2.0
print(round(2.1,-1))
# 0.0
# print(round(1.13,None))


# print(roundoff(2.13,1))

def roundoff(number, ndigits=None):
  if ndigits==None:
   return round(number) 

  return round(number,ndigits)



print(roundoff(12.14))
print(roundoff(12.14,1))
print(roundoff(13.13,0))

print(abs)
# <build-in function abs>


print(abs(-1))
print(abs(1.214))
print(abs(-1.214))
