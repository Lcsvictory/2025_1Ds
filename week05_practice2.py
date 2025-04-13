import random

class MinStack:
    def __init__(self):
        self.main = []
        self.min = []
        self.max = []
    
    def push(self, n):
        if len(self.main) == 0:
            self.min.append(n)
            self.max.append(n)
            self.main.append(n)
            return
        if n >= self.max[-1]:
            self.max.append(n)
        else:
            self.max.append(self.max[-1])
            
        if n <= self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.min[-1])

        self.main.append(n) 

    def pop(self):
        if len(self.main) == 0: return
        self.min.pop()
        self.max.pop()
        return self.main.pop()
    
    def get_min(self):
        return self.min[-1]
    
    def get_max(self):
        return self.max[-1]
    
    def __str__(self):
        return f"main : {self.main}\nmin : {self.min}\nmax : {self.max}"

def reverse_string(str):
    stack = list(str)
    result = ""
    while stack:
        result += stack.pop()
    return result


print(reverse_string("hello"))

minstack = MinStack()

for i in range(30):
    minstack.push(random.randint(1,100))

print(minstack)
print(minstack.get_min())
print(minstack.get_max())
minstack.pop()
minstack.pop()
minstack.pop()
print(minstack)
print(minstack.get_min())
print(minstack.get_max())

