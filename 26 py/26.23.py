with open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 26\\\\26-k2.txt') as t:
    t = [i.strip() for i in t]
n,k, m = list(map(int, t[0].split()))
del t[0]
t = list(map(int,t))
t.sort(reverse = True)
print(t[k+m-1], t[k-n-1])

