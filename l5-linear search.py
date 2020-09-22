#linear search
#definition for linear search
def linearsearch(a, x):
   for i in range(len(a)):
      if a[i] == x:
         return i
   return -1
a = [ 2, 3, 4, 10, 40 ]
x = 3
#printing the index of the searched element
print("element found at index "+str(linearsearch(a,x)))
