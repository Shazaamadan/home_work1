text='C:\\qq.txt'
infile=open(text, 'r')
deg=0
name= input('enter your name')
for i in range (20):
  s=infile.readline()
  print (s)
  an= input()
  a=an+'\n'
  s=infile.readline()
  if (s==a):
      deg+=1
text2='C:\\rus.txt'
result=open(text2,'w')
result.write(name)
result.write(str(deg))
result.close()
infile.close()