import re

pattern = r'\w+ \w+'
r = re.compile(pattern)
str = 'Hello world, ...'
m = r.match(str) # dopasowuje pare slow rozdzielonych spacja
if(m):
    print(m.group(0), "pasuje do wzorca", pattern)
else:
    print(str, "nie pasuje do wzorca", pattern)


pattern = r'(\w+) \1'
r = re.compile(pattern)

str = 'Hello world, ...'
m = r.match(str) # brak dopasowania
if(m):
    print(m.group(0), "pasuje do wzorca", pattern)
else:
    print(str, "nie pasuje do wzorca", pattern)

str = 'Hello Hello, ...'
m = r.match(str) # dopasowuje pare identycznych slow
if(m):
    print(m.group(0), "pasuje do wzorca", pattern)
else:
    print(str, "nie pasuje do wzorca", pattern)


pattern = r'(?P<word>\w+) (?P=word)'  # to samo co r'(\w+) \1' przy pomocy grupy nazwanej
r = re.compile(pattern)
m = r.match(str) # dopasowuje pare identycznych slow
if(m):
    print(m.group(0), "pasuje do wzorca", pattern)
    print(m.group('word'))
else:
    print(str, "nie pasuje do wzorca", pattern)


str = r'http://www.python.org'
pattern = r'(http://\w+(\.\w+)+)'
r = re.compile(pattern)
link = r.sub(r'<a href="\1">\1</a>', str)
print("link=", link)


str = r'http://www.python.org'
pattern = r'(?P<addr>http://\w+(\.\w+)+)'
r = re.compile(pattern)
link = r.sub(r'<a href="\g<addr>">\g<addr></a>', str)
print("link=", link)

