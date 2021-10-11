# a,b,c = 0
# Non-iterable Object
a,b,c = 0,0,0

a,b,c = [0,0,0]
# Array Destructing
a,b,c = [0,0],[1,1],[2,2]
# a,b,c = {0,0,0},0,0

# Object Literal

state = {
  'login': None,
  'signup': None,
  'user': {
    'name':'jai',
    'age':13
  }
}

# {} [] () set() - Pass by Reference
userRef = state['user']
# userRef['name'] = 'dev'
# print(userRef)

# Object Destructing
userVal = {**state['user']}
userVal['name'] = 'dev'
print(userVal);


print(state)
# print(state['login'])
x = dict(aa=dict(aaa=1,aaaa=2),bb=2,cc=3)
print(x.aa)
# print(x['aa'])
# print(x.aa)
# print(x['aa']['aaa'])

# a = [0,0,0]
# print(a,b,c)