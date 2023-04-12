T = int(input('횟수 입력 : '))

for i in range(T):
    a = input('연산 입력 : ').split()
    re = float(a[0])
    for i in a:
        if i == '@':
            re*=3 
        elif i =='%':
            re+=5
        elif i =='#':
            re-=7
    print('%0.2f' % re)
