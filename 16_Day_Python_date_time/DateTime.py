import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']


# Getting datetime Information
from datetime import datetime
now = datetime.now()
print(now)                      # 2021-03-10 22:35:23.770425
day = now.day                   # 10
month = now.month               # 3
year = now.year                 # 2021
hour = now.hour                 # 22
minute = now.minute             # 35
second = now.second             
timestamp = now.timestamp()     
print(day, month, year, hour, minute)
print('timestamp', timestamp)   # timestamp 1615395923.770425
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 10/3/2021, 22:35


# Formating Date Output Using strftime
from datetime import datetime
new_year = datetime(2021, 3, 10)
print(new_year)      # 2021-03-10 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) # 10 3 2021 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 10/3/2021, 0:0

# Time formating
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)               # time: 22:38:22
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)    # time one: 03/10/2021, 22:38:22
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)    # time two: 10/03/2021, 22:38:22


# String to Time Using strptime
from datetime import datetime
date_string = "10 March, 2021"
print("date_string =", date_string)     # date_string = 10 March, 2021
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)     # date_object = 2021-03-10 00:00:00


# Using date from datetime
from datetime import date
d = date(2021, 3, 10)
print(d)
print('Current date:', d.today())    # Current date: 2021-03-10
# date object of today's date
today = date.today()
print("Current year:", today.year)   # Current year: 2021
print("Current month:", today.month) # Current month: 3
print("Current day:", today.day)     # Current day: 10


# Time Objects to Represent Time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)     # a = 00:00:00
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)     # b = 10:30:50
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555


# Difference Between Two Points in Time Using
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)     # Time left for new year:  27 days, 0:00:00
t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)    # Time left for new year: 26 days, 23: 01: 00


# Difference Between Two Points in Time Using timedelata
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)       # t3 = 86 days, 22:56:50
