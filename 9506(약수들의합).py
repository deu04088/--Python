n = ''
list = []
def find(a):
    sum = 0
    for i in range(1,a):
        if a%i == 0:
            sum += i
            list.append(i)
    
    if sum == a:
        print('{} = {}'.format(a, list[0]), end = ' ')
        for i in range(1, len(list)):
            print('+ {}'.format(list[i]), end = ' ')
        print()
    else:
        print('{} is NOT perfect.'.format(a))    
    list.clear()
    
while True:
    n = int(input())
    if n == -1:
        break
    find(n)
    
# 좀 더 간소하게 sum() 과 join(), 리스트 컴프리헨션 사용
while True:
    n = int(input())
    if n == -1: 
        break
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")
    else:
        print(n, "is NOT perfect.")
        
#출처 : https://tturbo0824.tistory.com/35