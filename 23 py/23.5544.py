def f(start, end, counter = []): 
     counter = counter + [start] 
     if start == end: 
         for i in range(len(counter)-2): 
             if (counter[i] + counter[i+1] + counter[i+2]) % 11 == 0: 
                 return 1 
         return 0 
     if start > end: 
         return 0 
     return f(start + 2, end, counter) + f(start * 3, end, counter) + f(start * 4, end, counter) 
  
print(f(1, 600))