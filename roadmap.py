name = "victor"
age = str(15)
balance = 100.50
is_logged_in = True
print(f"my name is {name}")

print("c" in name)

list1 = [1, 2, 3, 4, 5]
list2 = list1
print(list1 is list2)

print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(balance))  # <class 'float'>
print(type(is_logged_in))  # <class 'bool'> 

print(name[1:4])  # 6


saved_password = "1234"

for i in range(3):
    password = input("Enter your password: ")
    if password.strip().lower()==saved_password:
        print("Access granted")
        break
    else:
        print(f"you have {3-(i+1)} attempts left")
else:
    print("Access denied", "you have exceeded the maximum number of attempts.")



fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "banana":
        print("Found banana!")
        break
