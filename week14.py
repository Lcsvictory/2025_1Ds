import math

def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0 : return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print((3, 2, 2) )

    s, e = map(int, input().split())
    for i in range(s, e+1):
        if is_prime(i):
            print(i)