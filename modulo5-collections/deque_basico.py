from collections import deque
d = deque([1, 2, 3])
print(d)

d.append(4)
d.appendleft(0)
print(d)

print(d.pop())
print(d.popleft())
print(d)

print(d[0], d[-1])
print(type(d), len(d), 1 in d)

vazio = deque()

try:
    vazio.popleft()
except IndexError as e:
    print(type(e).__name__, e)

