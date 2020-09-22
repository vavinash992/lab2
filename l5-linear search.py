arr = [6,29,34,55]
flag = 0
x = int(input("Enter the element to search: "))
for i in range(len(arr)):
    if arr[i] == x :
       flag = 1
       break      
if flag == 1:        
    print('Element found at '+ str(i))    
else:
    print('Element not found')
