import sys

stack = list()
n = int(input())
for i in range(n):
    order = sys.stdin.readline().strip()
    if "push" in order:
        number = int(order.split()[1])
        stack.append(number)
    elif "pop" in order:
        if len(stack) == 0: print(-1); continue
        print(stack.pop())
    elif "size" in order:
        print(len(stack))
    elif "empty" in order:
        print(1) if len(stack) == 0 else print(0)
    else:
        print(-1) if len(stack) == 0 else print(stack[-1])