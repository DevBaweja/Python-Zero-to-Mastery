# Prototype
# List(*list) : mylist
# mylist.get(index) : value
# mylist.set(index, value) : void
# mylist : [*list]

class List:
  def __init__(self,*mylist):
    print('List initialized');
    self.mylist = [*mylist]
    self.mylength = len(mylist)
  def __str__(self):
    string = ''
    for value in self.mylist:
      if value == self.mylist[-1]:
        string += str(value)
      else:
        string += f'{value}, '
    return f'[{string}]'
  def get(self,index):
    return self.mylist[index]
  def set(self, index, value):
    self.mylist[index] = value
  def length(self):
    return self.mylength

