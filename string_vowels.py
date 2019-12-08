st=input("Enter a string:")
st=st.upper()
cnt=0
for i in st:
	if(i=='A'or i=='E' or i=='I' or i=='O' or i=='U'):
		cnt += 1
print("No of Vowels :",cnt)
