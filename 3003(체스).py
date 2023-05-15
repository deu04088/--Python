chess = [1, 1, 2, 2, 2, 8]

find = list(map(int, input().split()))

for i in range(len(chess)):
    if find[i] == chess[i]:
        print(0, end = ' ')
    elif find[i] < chess[i]:
        print(chess[i] - find[i], end = ' ')
    else:
        print(chess[i] - find[i], end = ' ')