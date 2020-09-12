#to search a element in a array
def search(a,x): #defining a functio to search
    for i in range(len(a)):
        if(a[i]==x):
            return i
    return 'not found'
a=[1,2,3,5,9,24]
x=int(input("enter the number to be searched:"))
k=search(a,x)
#printing output
print("index of the entered number is:",k)
