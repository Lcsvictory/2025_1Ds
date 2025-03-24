import random
import math

n = 100
random_number = random.randint(1, n)
print(random_number)
win = False
count = 0
chance = int(math.log(n,2)) + 1

print(10*"*"+"guess game!"+10*"*")
while not win :
    if count >= chance:
        break
    user_input = int(input(f"[남은기회{chance - count}]1~{n}사이의 숫자를 입력하세요 : "))
    if user_input == random_number:
        win = True
        print(f"당신이 맞췄습니다. 정답 : {random_number}")
    elif user_input > random_number:
        count += 1
        print(f"정답보다 큽니다. 질문횟수 : {count}")
    elif user_input < random_number:
        count += 1
        print(f"정답보다 작습니다. 질문횟수 : {count}")
    else:
        print("잘못 입력하셨습니다.")

if win:
    print("축하합니다.")
else:
    print("안타깝습니다.")



