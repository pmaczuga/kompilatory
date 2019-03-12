import re

pattern = r'(\d+).(\d*)'
str = '342.79+12.56'

r = re.compile(pattern)
m = r.match(str)

print( m.group(0) )           # 342.79, cale dopasowanie
print( m.group(1) )           # 342, dopasowanie (\d+)
print( m.group(2) )           # 79, dopasowanie (\d*)
print( m.start(1), m.end(1) ) # 0, 3
print( m.start(2), m.end(2) ) # 4, 6
