T = int(input())
sum = []
for i in range(T):
    A, B = map(int, input().split())
    tmp = A + B
    sum.append(tmp)

for i in range(len(sum)):
    print('Case #{}: {}'.format(i+1, sum[i]))