no=int(input(""))
reverse=0
while(no>0):
  remainder=no%10
  reverse=(reverse*10)+remainder
  no=no//10
  print(reverse)
