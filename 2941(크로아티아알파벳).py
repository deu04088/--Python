cro_al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()

for i in cro_al:
    if i in alpha:
        alpha = alpha.replace(i, '*')

print(len(alpha))