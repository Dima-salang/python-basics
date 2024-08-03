num = int(input("Enter a number: "))
ones = num % 10
tenths = (num % 100) // 10
hundredths = (num % 1000) // 100
thousandths = (num % 10000) // 1000
tenThousandths = (num % 100000) // 10000
print(tenThousandths)
reversed = (ones*10000) + (tenths*1000) + (hundredths*100) + (thousandths*10) + (tenThousandths*1)

print("Ten Thousandth's Place: ", tenThousandths)
print("Thousandth's Place: ", thousandths)
print("hundredth's place: ", hundredths)
print("Tenth's Place: ", tenths)
print("One's Place: ", ones)

print("Reversed Number: ", reversed)


print((98 // 76 *5) + (43 % 21 * 1) - (23 // 45 + (6 % 7 + 8 // 9))