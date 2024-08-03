name = input("What is your name ?: ")
char_count_name = len(name)

if char_count_name < 3:
    print("Name must be at least 3 characters")
elif char_count_name > 50:
    print("Name can be a maximum of only 50 characters")
else:
    print("Name looks good !")

num1 = 5
num2 = 5
num3 = 4
print(num1 is num2)  # True
print(num1 is not num3)  # True

num_list = [1, 2, 3, 4, 5]
print(5 in num_list)  # True
print(6 not in num_list)  # True




