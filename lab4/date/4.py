#Write a Python program to calculate two date difference in seconds.
import datetime
import math
today = datetime.datetime.now()
today_without_m = (datetime.datetime(today.year, today.month, today.day, today.hour, today.minute, today.second, 0))

later_without_m = (datetime.datetime(2005, 11, 18, 1, 5, 25, 0))

diff = (later_without_m - today_without_m)
sec = diff.total_seconds()
print(math.fabs(sec))