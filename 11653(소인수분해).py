N = int(input())
a = 2

while N != 1:
    if N % a == 0:
        N = N//a
        print(a)
    else:
        a += 1
        
# 오래 걸리는 문제 해결 필요
       