a=input()
for i in range(len(a)):
  if(i%2==0):
    print(a[i+1],end='')
  else:
    print(a[i-1],end='')  
