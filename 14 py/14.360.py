s = '1234567890abcde'
j = '1234567890abc'
for a in range(1,1000):
    for x in s:
        for y in j:
            m = int(('2'+y+'23'+x+'5'),15)
            n = int(('67'+x+'9'+y),13)
            if (m+a)%n==0:
                print(a)