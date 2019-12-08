import random as rd
list1=[]
elem=20
for i in range(elem):
    list1.append(rd.randint(1,100))
print(list1)
sum=0
for i in list1:
    sum+=i
print("Avarage of list element:",sum/elem)
print("largest & smallest:",max(list1),"&",min(list1))
list1.sort()
print("second largest number:",list1[-2])
print("second smallest number is:",list1[2])
even=0
for i in list1:
    if (i%2==0):
        even+=1
print("total even number:",even)
