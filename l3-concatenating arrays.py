#program to concatenate arrays
a=int(input('enter the size of the array:'))
#creating a array
p=[None]*a
#taking input of elements of the array
print('enter the elements of first array')
for i in range(0,a):
    p[i]=int(input())
#creating second  array
b=int(input('enter the size of the second array:'))
q=[None]*b
#taking input of elements of the array
print('enter the elements of second array')
for j in range(0,b):
    q[j]=int(input())
#concatenating arrays
c=[]
c=p+q
print('after concatenating the array is',c)
