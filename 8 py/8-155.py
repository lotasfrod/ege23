from itertools import product
s = 'АИОУЭ'
words = list(map(''.join, product(s, repeat = 6)))
i = 0

for x in range(len(words)):
    if words[x][0] == 'О' and words[x][-1]=='О':
        i = x+1

print(i)