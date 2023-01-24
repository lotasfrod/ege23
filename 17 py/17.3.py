a = []
for x in range(117649, 823542 +1):
    if x%3 == 2 and x%8!=3 and x%12!=5:
        a.append(x)
print(len(a), max(a))