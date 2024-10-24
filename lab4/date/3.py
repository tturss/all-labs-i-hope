#Write a Python program to drop microseconds from datetime.
import datetime
today = datetime.datetime.now()
print(datetime.datetime(today.year, today.month, today.day, hour = today.hour, minute = today.minute, second = today.second, microsecond = 0))