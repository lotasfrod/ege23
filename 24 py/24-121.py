from re import S


with open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 24\\\\24-3.txt') as t:
    t = t.read()

max_len=0 #максимальная длина
max_ind = 0 #максимальный индекс

now_len = 0 #нынешняя длина
now_ind = 0 #нынешний индекс

state = True
for x in range(1,len(t)):
    if ord(t[x-1])> ord(t[x]):
        now_len +=1
        if state:
            now_ind = x-1
            state = False

    else:
        if now_len > max_len:
            max_len = now_len
            max_ind = now_ind
        now_len = -0
        state = True

print(max_ind+1)
