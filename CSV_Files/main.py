import csv

# 1
# with open('test.csv', 'w') as csv_file:
#     write = csv.writer(csv_file)
#     write.writerow(['user_id', 'user_name', 'comments_qty'])
#     write.writerow([5235, 'sergey', 13452])
#     write.writerow([456, 'john', 134])
#     write.writerow([87562, 'Alina', 88876])

# separate
with open('test.csv', 'w') as csv_file:
    write = csv.writer(csv_file, delimiter=';') # separate ;
    write.writerow(['user_id', 'user_name', 'comments_qty'])
    write.writerow([5235, 'sergey', 13452])
    write.writerow([456, 'john', 134])
    write.writerow([87562, 'Alina', 88876])

# 2 read from file test.csv

with open('test.csv') as csv_file:
   #  reader = csv.reader(csv_file)
    reader = csv.reader(csv_file, delimiter=';') # separate ;
    # print(reader)
    # print(type(reader))
    for line in reader:
        print(line)

    # csv_list = list(reader)
    # print(csv_list) # conv in list


