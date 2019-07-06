a=input()
for i in range(0,len(a)):
  if(a[i].isalpha() and a[i].digit()):
    print("No")
else:
  print("Yes")
