quote = 'to{}be{}or{}not{}to{}be'
print(quote.split('{}',-1))
capquote = []
for item in quote.split('{}'):
  capquote.append(item.capitalize())
print('{}'.join(capquote))