N, M = map(int, input().split())
box = [i for i in range(1, N+1)]

for a in range(M):
    i, j = map(int, input().split())
    box[i-1], box[j-1] = box[j-1], box[i-1]
    
for i in range(N):
    print(box[i], end = ' ')