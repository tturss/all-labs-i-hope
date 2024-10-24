#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def gen(n):
    for x in range(1, n):
        if x % 3 == 0 and x % 4 == 0:
            yield x

n = int(input("Enter the number: "))
for x in gen(n):
    print(x)