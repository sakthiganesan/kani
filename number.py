a,b=map(int,input().split())
for val in range(a,b+1): 
   if val > 1: 
       for num in range(2, val): 
           if (val % num) == 0: 
               break
       else: 
           print(val)
