l1=['HTTP','HTTPS','FTP','DNS']
l2=[80,443,21,53]
d={}
for i in range (len(l1)):
    d[l1[i]]=l2[i]
print (d)
