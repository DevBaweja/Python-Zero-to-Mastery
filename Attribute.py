a = {
  'key': 'value'
}
a['anotherkey']
# Key Error
# a.key 
# 'dict' object has no attribute 'key'
class th:
  def __init__(self):
    self.name = 'dev'
    pass
g = th()
# delattr(g,'name')
g.name
setattr(g,'age', 21)
print(g.age)

g['name']
# 'th' object is not subscriptable
