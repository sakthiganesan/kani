n=int(input(""))
sum = 0
temp = n
while (temp > 0):
  m=temp%10
   sum+=m**3
   temp //= 10
if (num == sum):
   print( "yes")
else:
   print("no")
