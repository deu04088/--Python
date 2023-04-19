T = int(input())

result = 0
tmp = 0
for i in range(T):
    answer = list(input())
    
    for i in range(len(answer)):
        if answer[i] == 'O':
            tmp += 1
            result += tmp
        else:
            tmp = 0
    
    print(result)
    result, tmp = 0, 0