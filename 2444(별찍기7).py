N = int(input())
for i in range(N):
    print(' '*(N-i-1), end = '')
    print('*','*'*2*i, sep = '')
    
for i in range(1, N):
    print(' '*i, end = '')
    print('*'*(2*N-2*i-1), sep = '')