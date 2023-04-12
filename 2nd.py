#code for using functions and for loop
#taking input
org=int(input("starting number of organisms:"))
aver=int(input("Average daily percentage increase:"))
fin=int(input("Enter the number of days to display the final data:"))
#showing headings
print("Day Approximate        Population")
print("------------------------------------------")
#declaring variables
a=0
i=0
#printing output
print(1,"                     ",org, "\n")
for i in range(1,fin):
  #calculations
  a=org+(org*(aver/100))
  org=a
  print(i+1,"                     ",a,"\n")
  i+=1

