import random

print(random.random())
print(random.randint(1, 10))  # number from 1 to 10

print(random.choice('abcd'))  # d
print(random.choice([1, 10, 4, 17]))

print(random.choices([10, 15, 20, 90, 120], k=2)) # for example [90, 15]

# shuffle
my_list = [1, 10, 4, 5, 15]
random.shuffle(my_list)
print(my_list) # my_list = [1, 10, 4, 5, 15]

# !!! not recommended for passwords
# generate password
# grouping elements into a string

print(''.join(random.choices('0123456789', k=8))) # 34722659
