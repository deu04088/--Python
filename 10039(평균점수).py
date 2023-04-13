list = []
for i in range(5):        
    list.append(int(input()))

sum = 0
for i in list:
    if i < 40:
        i = 40
        sum += i
    else:
        sum += i
        

print(int(sum/len(list)))