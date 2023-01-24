a = []
for x in range(2807, 8559):
    two = bin(x)[-2::] == '11'
    nine = x%9==5
    if two and nine:
        a.append(x)
print(max(a))