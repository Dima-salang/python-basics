# using stack to check if curr elem is equal to the popped elem
def is_palindrome(s):
    stack = []
    for n in s:
        stack.append(n)
    for i in range(0, len(stack)-1):
        if stack[i] == stack.pop() or len(stack) == 1:
            continue
        else:
            return False
    return True


# another method: traverse arr sequentially and check elem for every elem in reverse traverse
def is_palindrome_v2(s):
    return s[0:] == s[::-1]


print(is_palindrome('111'))
print(is_palindrome_v2('111'))
