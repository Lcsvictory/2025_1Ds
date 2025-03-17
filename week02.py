# shift + F10
n = int(input("정수 입력 : "))
result = 0
i = 1
while i <= n:
    result += i
    i += 1
print(f"1부터 n까지 누적합 = {result}")