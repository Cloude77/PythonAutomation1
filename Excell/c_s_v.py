import csv

def print_csv(csv_reader):
    for row in csv_reader:
        print(row)
read_file = open('C:/Users/SergeyML/Desktop/Excell/test_file.csv')
csv_reader = csv.reader(read_file)  # reader
print_csv(csv_reader)

append_data_to_file = open('C:/Users/SergeyML/Desktop/Excell/test_file.csv', 'a+', newline='') # open file , add new data
csv_writer = csv.writer(append_data_to_file) # writer file
csv_writer.writerow(['a', 'b', 'c', 'd'])
append_data_to_file.close()
print_csv(csv_reader)


