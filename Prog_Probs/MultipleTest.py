# Read two nteger values (A and B). After, the program should
# print the message "Sao Multiplos" (are multiples) or
# "Nao sao Multiplos" (aren’t multiples), corresponding to the read values.

def multiple_test(num, multiple):
    if multiple % num == 0:
        return True
    else:
        return False


print(multiple_test(5, 10))
