num=input()
l=len(num)
x01=[]
d=0
for x in range (l):
    if num[x]=='1':
       x01.append(1)
    else:
        x01.append(0)
for x in range (l):
  d=x01[x]*2**(l-1-x)+d
print (d)     