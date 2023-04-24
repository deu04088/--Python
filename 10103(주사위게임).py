n = int(input())
man1 = 100
man2 = 100

for i in range(n):
    num1, num2 = map(int, input().split())
    if num1 > num2:
        man2 -= num1
    elif num2 > num1:
        man1 -= num2
    else:
        pass
    
print(man1)
print(man2)