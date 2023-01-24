import sys
sys.setrecursionlimit(3493)
c = 0
def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1)+n

for n in range(765432010,1542613234):
    if f(n)%3!=0:
        c+=1
print(c)