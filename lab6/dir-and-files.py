import os, string
 #task 1
path = os.getcwd()
print(f"Files: {[a for a in os.listdir(path) if os.path.isfile(a)]}, directories: {[b for b in os.listdir(path) if os.path.isdir(b)]} all elements are: {os.listdir(path)}")


#task 2
path = r"C:\Users\turs\Desktop\dzz\pp\lab6\example.txt"
if os.path.exists(path):
    print("The path exists")
    
    if os.access(path, os.R_OK):
        print("The path is readable")
    else:
        print("The path is not readable")
    
    if os.access(path, os.W_OK):
        print("The path is writable")
    else:
        print("The path is not writible")

    if os.access(path, os.X_OK):
        print("The path is executable")
    else:
        print("The path is not executable")
else:
    print("The path does not exist")


#task 3
here = r"C:\Users\turs\Desktop\dzz\pp\lab6\example.txt"
if os.path.exists(here):
    print(os.path.basename(here))
    print(os.path.dirname(here))


#task 4
with open(r"C:\Users\turs\Desktop\dzz\pp\lab6\example.txt") as path:
    lines = len(path.readlines())
print(lines)


#task 5
list = str(input().split())
with open(r"C:\Users\turs\Desktop\dzz\pp\lab6\example.txt",'w') as here:
    here.write(list)


#task 6
for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as here:
        here.writelines(letter)


#task 7
with open(r"C:\Users\turs\Desktop\dzz\pp\lab6\example.txt",'r') as first:
    with open(r"C:\Users\turs\Desktop\dzz\pp\lab6\exx.txt",'w') as here:
        for line in first:
            here.write(line)


#task 8
if os.path.exists(r"C:\Users\turs\Desktop\dzz\pp\lab6\exx.txt"):
    os.remove(r"C:\Users\turs\Desktop\dzz\pp\lab6\exx.txt")
else:
    print("No file")
