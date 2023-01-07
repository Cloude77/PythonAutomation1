import time

print(time.time())
print(time.ctime()) # Thu Jan  5 14:35:51 2023  conversion

# stop program

time.sleep(2.5)
print(time.ctime())


# task execution time

start_time = time.time()

my_range = range(10000)
print(my_range[100])

my_list = list(range(100000))
print(my_list[1000]) # 1000 Total duration of the operation:  0.002000331878662109

end_time = time.time()
print("Total duration of the operation: ", end_time - start_time) # 100 Total duration of the operation:  0.0
