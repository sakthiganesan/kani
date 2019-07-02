m=input("")
b=0
for i in range(len(m)):
  if(m[i].digit() or m[i].alpha() or m[i]==("")):
    continue
  else:
    b+=1
    print(b)
