H, M, S = map(int, input().split())
D = int(input())

Sec = S + D
Min = M + (S+D)//60
Hour = H + (M + (S+D)//60)//60

print(Hour%24, Min%60, Sec%60)
        