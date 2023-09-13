def prost(n):
    
    for i in range(2,n//2+1):
        
        if n%i==0:
            return 0
    return 1

count=0
for i in range(2532421, 2532491):
    if prost(i):
        
        count+=1
        print(count,i)


