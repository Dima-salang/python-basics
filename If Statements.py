house_price = 1000000
has_goodcredit = True
no_goodcredit = False


if has_goodcredit:
    down_payment = 0.1 * house_price
elif no_goodcredit:
    down_payment = 0.2 * house_price
print(f"You need to pay: {down_payment}")
