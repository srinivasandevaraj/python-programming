n=input()
if(n.isnumeric()):
	a=int(n)
	if(1<=a<100000):
	  print (a)
	if(a%2==0):
		print("even")
	else:
		print("odd")
else:
	print("inva")
