import math

T = int(input())

for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0

    for j in range(n):
        x3, y3, r = map(int, input().split())
        dist1 = math.sqrt((x1-x3)**2 + (y1-y3)**2)
        dist2 = math.sqrt((x2-x3)**2 + (y2-y3)**2)
        
        if (r > dist1 and r > dist2) or (r < dist1 and r < dist2) :
            pass
        else:
            cnt += 1
            
    print(cnt)