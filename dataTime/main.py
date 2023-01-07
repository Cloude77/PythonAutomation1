from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

my_date = date(2028, 4, 15)
print(my_date.year)

print(my_date.isocalendar())

# time

my_time = time(18, 10, 45)
print(my_time)

print(my_time.minute)

# datetime

my_datetime = datetime(2028, 12, 12, 18, 10, 45)
print(my_datetime)

print(my_datetime.isoformat())
print(my_datetime.now())
print(my_datetime.now().microsecond)

# formatting

print(my_datetime.strftime('%d-%b-%Y'))  # 12-Dec-2028
print(my_datetime.strftime('%d-%b-%Y-%H-%M-%S'))  # 12-Dec-2028-18-10-45

# conversion

date_str = '12-Dec-2028'
converted_date = datetime.strptime(date_str, '%d-%b-%Y')
print(converted_date)  # 2028-12-12 00:00:00


# timedelta
# my_datetime = datetime(2028, 12, 12, 18, 10, 45) addition to this date

print(my_datetime + timedelta(days=20))  # 2029-01-01 18:10:45
print(my_datetime + timedelta(days=20, minutes=120))  # 2029-01-01 20:10:45


# module time

