f=open('error.py','r')
f1=open('copied.py','w')
for i in f:
	f1.write(i)
f.close()
f1.close()

