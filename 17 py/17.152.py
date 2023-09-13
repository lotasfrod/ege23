s = list(map(int, open('X:\\информатика\\задачи 17\\17-1.txt')))

ans = []

for i in range(len(s)-1):
    if (s[i]%9==0 and s[i+1]%9!=0 and abs(s[i+1])%8==3) or (s[i+1]%9==0 and s[i]%9!=0 and abs(s[i])%8==3):
        ans.append(max(s[i], s[i+1]))

print(len(ans), max(ans))

