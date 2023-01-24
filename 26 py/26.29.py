with open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 26\\\\26-j4.txt') as t:
    t = [int(i.strip()) for i in t]
ten_proc = t[0]//10
del t[0]
t.sort()
t = t[ten_proc::]
t = t[:len(t)-ten_proc:]
print(sum(t), t[-1])
