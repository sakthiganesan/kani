a=int(input(""))
num1=0
num2=1
count=0
while(count<a):
  print(num1,end=',')
  nth=num1+num2
  num1=num2
  num2=nth
  count+=1
