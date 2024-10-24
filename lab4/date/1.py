#Write a Python program to subtract five days from current date.
import datetime
today = datetime.datetime.now()
past = today - datetime.timedelta(days=5)
print(past)