def move_zeros(l):
    zero_index = 0 #0 자리를 알려주는 변수구나.
    for i,n in enumerate(l):
        if n != 0:
            l[zero_index] = n
            if zero_index != i: #제자리 바꿔치기가 아니라면.
                l[i] = 0
            zero_index += 1
    return(l)

temp_list = [23,44,0,-4123,312,0,222,0,321]
#temp_list = [23,44,-4123,0,312,0,222,0,321]
#temp_list = [23,44,-4123,312,222,0,0,321,0]

temp_list_move_zeros = move_zeros(temp_list)
print(temp_list)
print(temp_list_move_zeros)
