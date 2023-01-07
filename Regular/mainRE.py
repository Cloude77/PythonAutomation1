import re

my_string = "My name is Sergey"
my_string1 = "My name is Sergey."

res = re.search('^M.*name', my_string)  # match='My name'
res1 = re.search(r'S....y\.$', my_string1)  # match='Sergey.'

print(res.span()) # (0, 7) tuple
print(res.start()) # 0
print(res.end()) # 7
print(res1)
