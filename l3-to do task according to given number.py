#program  to do tasks according to given number
k=int(input())
a=[1,2,4,5,6,22,24,4,22,32]
def remove(a):#defining a function for removing duplicates
    final=[]
    for i in a:
        if i not in final:
            final.append(i)
    return final
def delete(a,pos): #defining function to delete element
    newlist = []  
    for x in range(len(a)):  
        if x!=pos:
            newlist.append(a[x])
    return newlist
def search(a,x): #defining a function to search
    for i in range(len(a)):
        if(a[i]==x):
            return i
    return 'not found'
if(k==1):
    b=[None]*len(a)
    for i in range(0,len(a)):
        b[i]=a[i]
    print("the copied array b=",b)
if(k==2):
    c=remove(a)
    print('array after removing duplicates is',c)
if(k==3):
    pos=int(input("enter the element index to be removed:"))
    n=delete(a,pos)
    print('after removing the element the array is',n)
if(k==4):
    x=int(input("enter the number to be searched:"))
    p=search(a,x)
    print("index of the entered number is:",p)
if(k==5):
    print('the contents of the array are:')
    for i in range(0,len(a)):
        print(a[i])
