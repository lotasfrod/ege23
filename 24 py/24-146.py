with open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 24\\24-j8.txt') as t:
    t = t.read()
t = t.replace('\n','') #или

#t = t.strip() или
maximum = 0
lenght = 0

for x in range(1, len(t)):
    if int(t[x-1])+int(t[x]) >=10:
        lenght+=1
    else:
        if lenght > maximum:
            maximum = lenght
        lenght = 0
print(maximum+1)


