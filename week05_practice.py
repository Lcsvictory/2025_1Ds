def is_valid_parentheses(expr : str) -> bool:
    stack = []
    for i in expr:
        if i == "(":
            stack.append(i)
        if i == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

def is_valid_brackets(expr : str) -> bool:
    stack = []
    brackets = {")" : "(", "}" : "{", "]" : "["}
    # print(brackets.values())

    for i in expr:
        if i in brackets.values():
            stack.append(i)
        if i in brackets:
            if len(stack) == 0 or stack.pop() != brackets[i]:
                return False

    return len(stack) == 0

# is_valid_brackets("안녕")

print(is_valid_brackets("([2+3])"))
print(is_valid_brackets("(2+{3*9})"))
print(is_valid_brackets("(2+(3*9)"))  # 스택에 여는 소괄호가 하나 남아 있어서 False
print(is_valid_brackets(")2+(3*9)("))