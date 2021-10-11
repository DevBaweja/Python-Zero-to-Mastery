a = 'lorem'
# Negative Index
print(a[-1])
print(a[-2])
# Full
print(a)
print(a[:])
# Slice
print(a[2:4])
# Step
print(a[2:4:2])
# Reverse
print(a[::-1])
# slice step cannot be zero

# [start:end:step]
# start - inclusive
# end - exclusive 

# str is immutable
a[0] = 'i'
# It works in list

# True - 1 False - 0 
a[True]
a[False]

