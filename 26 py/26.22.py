with open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 26\\\\26-k2.txt') as t:
    t = [i.strip() for i in t]
n,k = list(map(int, t[0].split()))

del t[0]
t = list(map(int,t))
for x in range(k):
    t.remove(max(t))
    t.remove(min(t))

print(max(t), sum(t)//len(t))