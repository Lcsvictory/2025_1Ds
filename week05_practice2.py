
class MinStack:
    def __init__(self):
        self.main = []
        self.min = []
    
    def push(self, n):
        if len(self.main) == 0:
            self.min.append(n)
        elif n <= self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.min[-1])
        self.main.append(n) 

    def pop(self):
        if len(self.min) == 0: return
        self.min.pop()
        return self.main.pop()
    
    def get_min(self):
        return self.min[-1]
    
    def __str__(self):
        return f"main : {self.main}\nmin : {self.min}"

def reverse_string(str):
    stack = list(str)
    result = ""
    while stack:
        result += stack.pop()
    return result


print(reverse_string("hello"))

minstack = MinStack()

minstack.push(20)
minstack.push(2)
minstack.push(6)
minstack.push(40)
print(minstack)
print(minstack.get_min())
minstack.pop()
print(minstack)
minstack.pop()
print(minstack)
minstack.pop()
print(minstack)
