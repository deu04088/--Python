N, M = map(int, input().split())
box = [i for i in range(1, N+1)]

for a in range(M):
    i, j = map(int, input().split())
    tmp = box[i-1:j]
    tmp.reverse()
    box[i-1:j] = tmp

for i in range(N):
    print(box[i], end = ' ')
    
# C 언어 개념으로 생각하지 말 것