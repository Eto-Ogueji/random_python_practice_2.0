import math

for i in dir(math):
    print(i, end="\n")
    print("------------")
    print(help(i))
