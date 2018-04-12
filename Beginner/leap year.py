a=int(input("Enter the year:"))
if(a%100==0):
  if(a%400==0):
    print("yes")
  else:
    print("no")
elif(a%4==0):
  print("yes")
else:
  print("no")
