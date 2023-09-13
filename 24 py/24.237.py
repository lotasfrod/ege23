with open('X:\\информатика\\задачи 24\\24-237.txt') as t:
    t = t.readline()

col =0
ma= 0
for x in range((len(t)-2)):
    if t[x]==t[x+1]==t[x+2]:
        for y in range(x,len(t)-2,3):
            if t[y]==t[y+1]==t[y+2]:
                col+=3
            else:
                break
        ma = max(col,ma)
        col = 0
print(ma)

