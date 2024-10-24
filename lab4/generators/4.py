#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for x in range(a, b + 1):
        yield x ** 2

a = int(input("Enter lower bound: "))
b = int(input("Enter upper bound: "))

for k in squares(a, b):
    print(k)