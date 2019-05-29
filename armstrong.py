num = int(input(""))
sum = 0
temp = num
while (temp > 0):
   m = temp % 10
   sum += m ** 3
   temp //= 10
if (num == sum):
   print("an Armstrong number")
else:
   print(" not an Armstrong number")
