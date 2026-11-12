
for number in range(1, 101):
    if number % 2 == 0 and number % 3 == 0:
            print(f"{number} fizzbuzz")
    elif number % 2 == 0 :
        print(f"{number} fizz")
    elif number % 3 == 0:
        print(f"{number} buzz")
   
    else:
        