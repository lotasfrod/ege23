data = list(map(int,open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-202.txt').readlines()))

def cond(x):
  return 100 <= x < 1000 and x % 100 == 12

ma = 0
count = 0
for i in range(2,len(data)):
  if (not cond(data[i-2])) and cond(data[i-1]) and (not cond(data[i])):
    count += 1
    ma = max(ma, sum(data[i-2:i+1]))

print( count, ma)
