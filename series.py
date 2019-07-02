num=int(input())
fib1,fib2=0,1
print(fib2,end=" ")
for i in range(1,num):
  fib3=fib1+fib2
 print(fib3,end=" ")
 fib1,fib2=fib2,fib3

