def insertionsort(a):
	for i in range(1,len(a)):
		ele = a[i]
		pos = i-1
		while pos>=0 and a[pos]>ele:
			a[pos+1] = a[pos]
			pos -= 1
		a[pos+1] = ele
	print("insertionsort :   ",a)

# Taking array input
l = list(map(int,input("Enter elements to sort: ").split()))
insertionsort(l)
