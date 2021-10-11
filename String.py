class String: 
  def __init__(self,s):
    self.s = s
    # Representational Functions/Methods
  def __str__(self):
    return self.s
  # def show(self):
  #   return self.s
  def format(self,args):
      self.s = self.s.replace('{}', args, 1)
      return self
private = 'secret'