#code for calculating yearly rainfall and average monthly rainfall 
#taking input 
a=0
y=int(input("Enter the number of years:"))
print("for",y,"year")
#applying while loop
while(a<y):
   #declaring variables
   i=0
   total=0
   aver=0
   #again applying while loop
   while(i<12):
    print ("enter the rainfall amount for the month-",i+1)
    b=int(input())
    i+=1
    #calculating total
    total=total+b
    #result
   print("Total Rainfall:",total,"centimetres")
   #for calculating average
   aver=total/12
   #result of average
   print("Average Monthly Rainfall=",aver,"centimetres")
   a=a+1
    
