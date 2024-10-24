#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i


n = int(input("Enter a number: "))
even_gen = even_numbers(n)
even_list = list(even_gen)
print("Even numbers between 0 and", n)
print(*even_list, sep=", ")