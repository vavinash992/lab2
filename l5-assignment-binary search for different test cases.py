#Defining the function binary Search
def binary_search(a, x): 
	low = 0
	high = len(a) - 1
	mid = 0
	while low <= high: 
		mid = (high + low) // 2
		if a[mid] < x: 
			low = mid + 1
		elif a[mid] > x: 
			high = mid - 1
		else: 
			return mid  
	return 'not found'
#Test Case 1 : entering or passing the element that is not present in
print ( 'Test case 1: ')
arr1 = [10,20,30,-50,22,34]
s1 = -19
result = binary_search(arr1,s1)
print("Element is present at index", str(result)) 

#Test Case 2 : Entering the middle element of the array
print ( 'Test case 2 : ')
arr2 = [10,20,30,54,-50,22,34]
s2= 54
result = binary_search(arr2,s2)
print("Element is present at index", str(result)) 

#Test Case 3 : Entering same number twice
print ( 'Test case 3 : ' )
arr3 = [0, 22,25,35, 0, 565, -9]
s3 = 0
result = binary_search(arr3,s3)
print("Element is present at index", str(result)) 
