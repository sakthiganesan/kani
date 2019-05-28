a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
if(a>b):
  if(a>c):
    print(a)
  else:
    print(c)
elif(b>a):
  if(b>c):
    print(b)
  else:
    print(c)
elif(c>a):
  if(c>b):
      print(c)
else:
  print("invalid input")
