import re

pattern = r'(\d+)\.(\d*)'
str = 'a + 342.79+ b + 12.56 * 10'
r = re.compile(pattern)

m = r.match(str)   # brak dopasowania

m = r.search(str)  # dopasowuje pierwsza liczbe zmiennoprzecinkowa, tj. 342.79
if m:
    print(m.group() )


floats = [ x[0] for x in re.findall( r'((\d+)\.(\d*))', str) ]
print("floats=", floats)

for m in r.finditer(str):
    print(m.group())

list = [ m.group() for m in r.finditer(str) ]
print("list=", list)

terms = re.split("\s*[+*]\s*", str);
print(terms)

terms = re.split("(\s*[+*]\s*)", str);
print(terms)


newstr = r.sub("\\2.\\1", str);
print(str)
print(newstr)

print( r.subn(r"\2.\1", str) );

s = "http://python.org"
pattern = r'(http://[\w]+(.[\w]+)*(/[\w~]*)?)'
r = re.compile(pattern)
s2 = r.sub(r'<a href="\1">\1</a>', s)
print(s2)
