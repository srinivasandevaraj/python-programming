a=int(input("Enter the year:"))
if(a%100==0):
  if(a%400==0):
    print("Yes")
  else:
    print("No")
elif(a%4==0):
  print("Yes")
else:
  print("no")
