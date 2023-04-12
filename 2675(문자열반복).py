T = int(input("횟수 입력 : "))

for i in range(T):
    cnt, w = input('횟수 및 단어 입력 : ').split()
    for i in w:
        print(i*int(cnt), end='')
    print()