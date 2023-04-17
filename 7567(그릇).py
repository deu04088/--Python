str = input()
list = list(str)
sum = 10

for i in range(1, len(list)):
    if list[i-1] != list[i]:
        sum += 10
    else:
        sum +=5
        
print(sum)


