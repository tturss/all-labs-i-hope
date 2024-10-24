#Write a Python program to print yesterday, today, tomorrow.
import datetime
today = datetime.datetime.now()

print("Yesterday time: ", today - datetime.timedelta(days=1))
print("Today time: ", today)
print("Tomorrow time: ", today + datetime.timedelta(days=1))