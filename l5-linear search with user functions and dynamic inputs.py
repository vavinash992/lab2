# Implement linear search with user functions and dynamic inputs
#creating an array and taking input values
a=[]
n=int(input("enter number of elements to be entered into array: "))
for i in range(0,n):
    x=int(input("enter the element:"))
    a.append(x)
#definition for linear search
def linearsearch(a, x):
   for i in range(len(a)):
      if a[i] == x:
         return i
   return 'not found'
x=int(input("enter the value to be searched:"))
#printing the index of the searched element
print("element found at index "+str(linearsearch(a,x)))
