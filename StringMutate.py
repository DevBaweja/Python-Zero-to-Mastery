a = 'lorem'
def mutate(string,index,char):
  return '{1}{0}{2}'.format(char,string[:index],string[index:])

print(mutate(a,2,'w'))
