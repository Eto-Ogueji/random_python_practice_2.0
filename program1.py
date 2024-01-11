firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = input("Enter your age: ")

info = {
    'First Name': firstName,
    'Last Name': lastName,
    'Age': age
}
print("Your credentials: \n")
for i in info:
    if i == 'First Name':
        print("Your name is {}".format(firstName))
    if i == 'Last Name':
        print("Your name is {}".format(lastName))
    if i == 'Age':
        print("You are {} years old".format((age)))
