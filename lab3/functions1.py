
import math
from itertools import permutations

# Task 1: Convert Grams to Ounces
def grams_to_ounces(grams):
    return grams / 28.3495231

# Task 2: Fahrenheit to Centigrade Conversion
def fahrenheit_to_centigrade(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# Task 3: Solve the Classic Puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if chickens * 2 + rabbits * 4 == numlegs:
            return chickens, rabbits
    return None, None

# Task 4: Filter Prime Numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Task 5: Permutations of a String
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Task 6: Reverse Words in a Sentence
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

# Task 7: Check if List Contains 3 Next to a 3
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Task 8: Check if List Contains 007 in Order
def spy_game(nums):
    code = [0, 0, 7]
    code_idx = 0
    for num in nums:
        if num == code[code_idx]:
            code_idx += 1
        if code_idx == len(code):
            return True
    return False

# Task 9: Compute Volume of a Sphere
def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

# Task 10: Return Unique Elements of a List
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

# Task 11: Check if Word or Phrase is a Palindrome
def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

# Task 12: Print a Histogram
def histogram(lst):
    for n in lst:
        print('*' * n)

# Task 13: Guess the Number Game
def guess_the_number():
    import random
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break


if __name__ == "__main__":
    grams = 100
    ounces = grams_to_ounces(grams)
    print(f"{grams} grams is equal to {ounces:.2f} ounces.")

    # Task 3: Solve the Classic Puzzle
    numheads = 35
    numlegs = 94
    chickens, rabbits = solve(numheads, numlegs)
    if chickens is not None:
        print(f"There are {chickens} chickens and {rabbits} rabbits.")
    else:
        print("No solution found.")

    # Task 11: Check if Word or Phrase is a Palindrome
    word = "madam"
    if is_palindrome(word):
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")

    # Task 13: Guess the Number Game
    guess_the_number()
