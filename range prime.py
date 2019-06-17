a,b=map(int,input().split())
num=[]
for i in range(a,b+1):
  count=0
  for j in range(2,i+1):
    if(i%j==0):
      count=count+1
  num.append(count)
print(num.count(1))  
