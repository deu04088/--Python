T = int(input())

for i in range(T):
    N = int(input())
    zero, one = 1, 0
    for i in range(N):
        zero, one = one, zero + one
    print(zero, one)
    
# 더 공부해야할 필요가 있음
# 이해불가