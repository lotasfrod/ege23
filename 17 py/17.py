count = 0
ma = 0
for x in (1104,11001,6):
    state = True
    for y in (7,17,13,23):
        if x%y==0:
            state = False
            break

    if state:
        count +=1
        if x>ma:
            ma=x
print(count,ma)

