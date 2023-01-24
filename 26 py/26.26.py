with open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 26\\\\26-j1.txt') as t:
    t = [int(i.strip()) for i in t][1::]
col = 0
s = t[::]
for i in t:
    if (100-i) in s and i in s:
        col+=1
        s.remove(i)
        s.remove(100-i)
print(col)