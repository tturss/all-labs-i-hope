#Implement a generator that returns all numbers from (n) down to 0.
def rev(n):
    for x in range(n, -1, -1):
        yield x

a = int(input("Enter the number: "))
for k in rev(a):
    print(k)