T = int(input())

for i in range(T):
    N = int(input())
    dic = {}
    amon_list = []
    for i in range(N):
        s_name, amount = input().split()
        dic[s_name] = int(amount)
        amon_list.append(int(amount))
    reverse_dic = dict(map(reversed, dic.items()))
    print(reverse_dic[max(amon_list)])
