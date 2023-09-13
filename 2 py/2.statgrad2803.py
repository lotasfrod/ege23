print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not((x<=y)==(w or not z)) and ((x<=y) and (not w ==z)):
                    if [x,y,z,w].count(0)>=3:
                        print(x,y,z,w)
print('\n')
print('x y z w')

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not((x<=y)==(w or not z)):
                    if [x,y,z,w].count(0)>=3:
                        print(x,y,z,w)


print('\n')
print('x y z w')

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not((x<=y) and (not w ==z)):
                    if [x,y,z,w].count(1)>=2 and z==1 and y!=w:
                        print(x,y,z,w)


