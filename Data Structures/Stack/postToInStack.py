from collections import deque

post_stack = deque()

post_stack.append("A")
post_stack.append("B")
post_stack.append("*")
post_stack.append("C")
post_stack.append("D")
post_stack.append("+")
post_stack.append("-")
post_stack.append("E")
post_stack.append("+")

operand_stack = deque()
infix_stack = deque()

for i in post_stack:
    if i.isalnum():
        operand_stack.append(i)
    elif i in ["+", "-", "*", "/"]:
        operator2 = operand_stack.pop()
        operator1 = operand_stack.pop()
        infix = f"({operator1} {i} {operator2})"
        operand_stack.append(infix)
    
print(operand_stack)


