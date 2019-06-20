a,b=input().split()
count=0
for j in range(len(a)):
  if a.count(a[j])==b.count(b[j]):
    count=+1
  if count==len(a):
    print("yes")
  else:
    print("no")
