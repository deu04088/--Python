T = int(input())

for i in range(T):
    Yonsei = []
    Korea = []
    Y, K = 0, 0
    for i in range(9):
        Y, K = map(int, input().split())
        Yonsei.append(Y)
        Korea.append(K)
        
    if sum(Yonsei) > sum(Korea):
        print('Yonsei')
    else:
        print('Korea')

# 좀 억지스러운 부분이 있는 문제...