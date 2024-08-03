prices = [20, 30, 40]
total = 0
for calculation in prices:
    total += calculation

print(total)

for items in range(100):
    print(items)

numbers = [5, 2, 5, 2, 2]
variable = "x"
for x in numbers:
    print("x" * x)

def get_sum(a, b):

    if a == b:
        return a
    else:
        sum_list = 0
        for num in range(a, b):
            sum_list += num
        print(sum_list)


get_sum(1, 3)

