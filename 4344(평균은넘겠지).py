C = int(input())

for i in range(C):
    info = input()
    score = [int(j) for j in info.split()]
    average = sum(score[1:]) / score[0]
    
    cnt = 0
    for k in score[1:]:
        if k > average:
            cnt += 1
    print(f'{cnt/score[0]*100:.3f}%')
    
# for문 범위 지정 때문에 틀린 것으로 채점