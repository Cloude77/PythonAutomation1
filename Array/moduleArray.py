from array import array

my_int_array = array('i', [4, 10, 5, 7, 5])
print(my_int_array)  # only int number

my_int_array.append(15)
print(my_int_array)  # array('i', [4, 10, 5, 7, 15])

print(end='========================================\n\n')
# count - identical elements
print(my_int_array.count(5))  # 2

my_int_array.pop()
print(my_int_array)  # array('i', [4, 10, 5, 7, 5])

for elem in my_int_array:
    print(elem)

# writing to binary

with open('my_array.bin', 'wb') as my_file:
    my_int_array.tofile(my_file)

# data from file. Create empty array

imported_array = array('i')

with open('my_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 3)
    print(imported_array) # array('i', [4, 10, 5])

imported_array.reverse()
print(imported_array) # array('i', [5, 10, 4])
