x = y = [7, 8, 9]
x = [13, 4, 5]


print(x)
print(y)

name = True + False
print(name)

a = reversed('etoskie')

print(a)

a = (1, 2, 3)
print(a[1])

# Strings and tuples are immutable, while lists, dictionaries, and sets are mutable.

# but in this case

a = [1, 2, 3]
b = ['a', 1, 'python', (1, 2), [1, 2]]
print(b[3][1])

login = {
    'first': [1, 2, 3],
    'second': "a string"
}

x = None
if x is None:
    print("Fuck off!")


domain = ['hello', 'I', 'am', 'eto']
labs = list(a)
labs1 = set(a)
labs2 = tuple(a)

print(labs)
print(labs1)
print(labs2)

print(b'foo bar')