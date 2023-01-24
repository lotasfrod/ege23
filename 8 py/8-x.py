from itertools import permutations
s = 'НОБЕЛИЙ'
words = list(map(''.join,permutations(s,7)))
count = 0
for x in words:
    if x[0] != 'Й' and 'ИЙО' not in x:
        count+=1
print(count)