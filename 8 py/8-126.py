from itertools import product
s = 'АОУ'
words = list(map(''.join, product(s, repeat = 5)))[::-1]
print(words[99])