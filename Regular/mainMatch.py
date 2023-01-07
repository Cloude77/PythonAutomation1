import re

my_string = "My name is Sergey."

my_pattern = re.compile(r'^My.*\.$')
print(my_pattern)
print(my_pattern.match(my_string)) #  match='My name is Sergey.'



my_string1 = "My name is Sergey.Sergey is a junior programmer"
my_pattern1 = re.compile(r'S....y')
print(my_pattern1.findall(my_string1)) # ['Sergey', 'Sergey']