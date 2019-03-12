
import re

pattern = r'(\d+).(\d*)'
str = '342.79+12.56'

m = re.match(pattern,str)
if m:
    print("{0} pasuje do {1}".format(pattern, str) )
else:
    print("{0} nie pasuje do {1}".format(pattern, str) )