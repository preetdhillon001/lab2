#declaring variable
a=[]
j=0
#loop for taking numbers from user
while(j<10):
  a.append(int(input("entre number:")))
  j=j+1
#output
print("list of numbers:\n")
a.sort()
print(a)
#again declaring variable
c=[]
j=0
while(j<12):
  if(a[j]>12):
    c.append(a[j])
  else:
    pass
  j=j+1
print("List of numbers that are greater than 12:")
print(c)

  
  
  
  

