# 1. Class to Get and Print a String
class StringHandler:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input(" a string pls: ")

    def printString(self):
        print(self.s.upper())
sh = StringHandler()
sh.getString()
sh.printString()

# 2. Shape and Square Classes

class Shape:
    def area(self):
        return 0

class square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
square = square(4)
print("square area:", square.area())

# 3. Rectangle Class

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
rectangle = Rectangle(4, 5)
print("Rectangle area:", rectangle.area())

# 4. Point Class

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
p1 = Point(1, 2)
p2 = Point(4, 6)
p1.show()
p2.show()
print("Distance between points:", p1.dist(p2))

# 5. Bank Account Class
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, new balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance is {self.balance}")
acc = Account("Almas Saduakas", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(150)

# 6. Filtering Prime Numbers

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)
