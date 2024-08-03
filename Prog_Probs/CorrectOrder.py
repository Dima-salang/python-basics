# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# We can use a stack to keep track of whether nth elem of the string is in the dict keys.

def correct_order(s):
    stack = []
    chars = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    for n in s:
        if n in chars:
            stack.append(n)
        elif len(stack) == 0 or chars[stack.pop()] != n:
            return False
    return len(stack) == 0


print(correct_order('[]{}'))