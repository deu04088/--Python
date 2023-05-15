dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = list(input())

sum = 0
for i in S:
    for j in dial:
        if i in j:
            sum += dial.index(j)+3

print(sum)