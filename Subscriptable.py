a = {
  'name': 'dev'
}

print(a['name'])
# Subscriptable
print(a.name)
# Attr error

class th:
  def __init__(self):
    self.name = 'dev'
  def format(self):
    pass
g = th()

print(g.name)
# Attr
print(g['name'])
# Not Subscriptable