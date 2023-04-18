N = int(input())
num =[]
for i in range(N):
    num.append(input())
    
if num.count('1') > num.count('0'):
    print('Junhee is cute!')
elif num.count('1') < num.count('0'):
    print('Junhee is not cute!')