from itertools import product
c = 'ABCDX'
z = list(product(c,repeat= 4))
answer = list(filter(lambda x: x.count('X')==1,z))
print(len(answer))
