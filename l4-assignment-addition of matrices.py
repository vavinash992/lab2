n = int(input('Enter the value of N in NxN matrix: '))

print('''\nThis is a Sparse matrix.
So input high frequency of zeros.\n''')
# taking values of first matrix:
print("Enter the values for the first matrix : ")
a= []
for i in range(n):
    print('Enter the values for {i}th row : ')
    x=[]
    for j in range(n):
      x.append(int(input()))
    a.append(x)
# taking values of second matrix:
print('Enter the values for the Second Matrix :')
b =[]
for i in range(n):
    print(f'Enter the values for {i}th row : ')
    x=[]
    for j in range (n):
        x.append(int(input()))
    b.append(x)

#creating a matrix to store
n = [[0 for j in range(n)]for i in range(n)]
#adding two sparse matrices and storing in other matrix
for i in range(len(a)):
    for j in range(len(a[0])):
        n[i][j] = a[i][j] + b[i][j]

print('The sum of the two sparse matrices is :')
for r in n:
    for y in r:
        print(y, end = " ")
    print()
#representing the sparse matrix:
sparse_matrix = []
for i in range(len(n)):
    for j in range(len(n[0])):
        if n[i][j] != 0 :
            temp = []
            temp.append(i)
            temp.append(j)
            temp.append(n[i][j])
            sparse_matrix.append(temp)

print('''The Sparse Matrix representation :
Row\tCol\tValue''')
for i in sparse_matrix:
    for j in i:
        print(j,end = ' \t ')
    print()
