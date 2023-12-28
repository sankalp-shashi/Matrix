import matrix
x=0
print("Welcome!")
print("To add two matrices, enter 0")
print("To subtract two matrices, enter 1")
print("To find the minor of a matrix, enter 2")
print("To find the determinant of a matrix, enter 3")
print("To multiply two matrices, enter 4")
print("To find the inverse of a matrix, enter 5")
print("To find the rank of a matrix, enter 6")
x=int(input(": "))

M1=[]
M2=[]
if x==0:
    matrix.store(M1)
    matrix.display(M1)
    matrix.store(M2)
    matrix.display(M2)
    matrix.display(matrix.add(M1,M2))
    p=0
    p=input("Hit enter to close")
    
elif x==1:
    matrix.store(M1)
    matrix.display(M1)
    matrix.store(M2)
    matrix.display(M2)
    matrix.display(matrix.subtract(M1,M2))
elif x==2:
    matrix.store(M1)
    matrix.display(M1)
    print("The minor is: ")
    matrix.display(matrix.minor(M1))
elif x==3:
    matrix.store(M1)
    matrix.display(M1)
    print("The determinant is: ",matrix.det(M1))
elif x==4:
    matrix.store(M1)
    matrix.display(M1)
    matrix.store(M2)
    matrix.display(M2)
    matrix.display(matrix.mult(M1,M2))
elif x==5:
    matrix.store_square(M1)
    matrix.display(M1)
    if matrix.det(M1)!=0:
        print()
        print("The inverse is: ")
        M2=matrix.inv(M1)
        matrix.display(M2)
    else:
        print("This matrix is a singular matrix, it does not have an inverse.")
elif x==6:
    matrix.store(M)
    print("The matrix is: ")
    matrix.display(M)
    print("The rank is: ", matrix.rank(M))


p=0
p=input("Hit enter to close")
