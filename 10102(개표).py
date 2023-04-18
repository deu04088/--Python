V = int(input())
list = list(input()) 

if list.count('A') > list.count('B'):
    print('A')
elif list.count('A') < list.count('B'):
    print('B')
else:
    print('Tie')

# 심사위원 수를 받을 이유가 있을까...?
