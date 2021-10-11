class string: 
  def __init__(self,s):
    self.s = s

  def format(self,args):
      self.s = self.s.replace('{}', args)


first = 'dev'
mystring = string('Hi I am {}')
mystring.format(first)

last = 'baweja'
mystr = string('Hi, {}')
mystr.format(last)

print(mystr)
print(mystring)