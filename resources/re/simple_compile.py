
import re

pattern = r'(\d+).(\d*)'
str = '342.79+12.56'

r = re.compile(pattern)
m = r.match(str)
if m:
    print("{0} pasuje do {1}".format(pattern, str) )
else:
    print("{0} nie pasuje do {1}".format(pattern, str) )
