a=int(input(""))
if(a>0):
  for i in range(2,a//2):
    if(a%i==0):
      print("no")
      break
  else:
    print("yes")
else:
  print("no")
