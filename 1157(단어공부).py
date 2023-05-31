word = list(input().upper())
s_word = list(set(word))
cnt_li = []

for i in s_word:
    if i in word:
        cnt = word.count(i)
        cnt_li.append(cnt)

if cnt_li.count(max(cnt_li)) > 1:
    print('?')
else:
    print(s_word[cnt_li.index(max(cnt_li))])
