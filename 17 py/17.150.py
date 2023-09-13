s = list(map(int, open('X:\\информатика\\задачи 17\\17-1.txt')))

answer = []
for i in range(len(s)-1):
    if (s[i]%7==0 and s[i+1]%17!=0) or (s[i+1]%7==0 and s[i]%17!=0):
        answer.append(s[i]+s[i+1])

print(len(answer), min(answer))


