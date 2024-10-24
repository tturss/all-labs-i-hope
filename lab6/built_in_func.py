import math, time

#task 1
list = [1,2,3,4,5,6,7]
print(math.prod(list))


#task 2
def count(str):
    upp=0
    low=0
    for i in range(len(str)):
        if str[i]>='a' and str[i] <= 'z':
            low += 1
        elif str[i]>='A' and str[i] <= "Z":
            upp += 1
    print(f"Uppercase leters: {upp} \nLowercase letters: {low}")
str = input()
count(str)

#task 3
string = input()
def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome(string))


#task 4
def root(milsec, n):
    time.sleep(milsec/1000)
    return math.sqrt(n)
n = int(input("Sample Input:\n"))
milsec = int(input())
print("Sample Output:")
print(f"Square root of {n} after {milsec} is {root(milsec,n)}")


#task 5
tuple = (True,1,"Hello",True)
print(all(tuple))