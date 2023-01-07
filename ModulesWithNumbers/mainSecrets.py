import secrets
import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)

# print(string.ascii_letters + string.digits + string.punctuation)

# generate password

all_chears = string.ascii_letters + string.digits + string.punctuation

print(secrets.choice(all_chears)) # for example ( choice only 1 element
print(secrets.choice(all_chears) for i in range(8))

# form a string from 8 symbols

print(''.join(secrets.choice(all_chears) for i in range(8))) # LvzeJZH%

