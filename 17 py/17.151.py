s = list(map(int, open('X:\\информатика\\задачи 17\\17-1.txt')))

count = 0
min1 = []
for i in range(len(s)-1):
    if (abs(s[i])%10==6 and abs(s[i])%3==0) or (abs(s[i+1])%10==6 and abs(s[i+1])%3==0):
        count+=1
        min1.append(min(s[i], s[i+1]))
print(count, min(min1))
