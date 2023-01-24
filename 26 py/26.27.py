with open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 26\\\\26-j2.txt') as t:
    t = [int(i.strip()) for i in t][1::]
t.sort()
srzn  = (sum(t)//len(t))+1
median = t[len(t)//2]
s = 0
for x  in range(srzn, median+1):
    s+=t.count(x)
print(s)