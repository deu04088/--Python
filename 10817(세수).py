#1
A, B, C = map(int, input().split())

if A >= B:
    if B >= C:
        print(B)
    else :
        print(C)
elif B >= C:
    if C >= A:
        print(C)
    else:
        print(A)
else:
    if B >= A:
        print(B)
    else:
        print(A)
    
#2
num = list(map(int, input().split()))
num.sort()
print(num[1])