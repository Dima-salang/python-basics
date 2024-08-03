from collections import deque

newQueue = deque()  # initialize deque
newQueue.append("h")
newQueue.append("e")
newQueue.append("l")
print(newQueue)

print(newQueue.popleft())  # pop from head
print((newQueue.pop()))  # pop from tail


