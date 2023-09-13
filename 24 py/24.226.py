with open('X:\\информатика\\задачи 24\\24-225.txt') as t:
    t = t.readline()
t = t.split('C')
maximum = 0
for x in t:
    if x[0:3] == '234' and x[6:8] == '57' and x[-1] == '8' and len(x) == 12:
        maximum = max(maximum, int(x))

answer = 1
for x in str(maximum):
    if x in '13579':
        answer *= int(x)
print(answer)
