with open('X:\\информатика\\задачи 24\\24-191.txt')as t:
    t = t.readline()

col = 0
now_string = ''
for x in range(len(t)):
    if t[x] == 'A':
        now_string += 'A'
        for y in range(x + 1, len(t)):
            if t[y] == 'A':
                break
            elif t[y] == 'B':
                if now_string.count('F')==2 and len(now_string) >=19:
                    col += 1
                break
            else:
                now_string += t[y]
        now_string = ''
print(col)