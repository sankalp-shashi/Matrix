import sys

########################################################################################################################################################################################
def product(a):
    z=1
    for i in range(len(a)):
       z=z*a[i]
    return z


########################################################################################################################################################################################
def store(M):
    r=int(input("Enter number of rows of matrix: "))
    c=int(input("Enter number of columns of matrix: "))
    for i in range(r):
        a=[]
        for j in range(c):
            x=int(input(f"The entry of row {i+1}, column {j+1} is: "))
            a.append(x)
        M.append(a)
    return M


########################################################################################################################################################################################
def store_square(M):
    n=int(input("Enter the order of the matrix: "))
    for i in range(n):
        a=[]
        for j in range(n):
            x=int(input(f"The entry of row {i+1}, column {j+1} is: "))
            a.append(x)
        M.append(a)
    return M


########################################################################################################################################################################################
def display(M):
    print()
    r=len(M)
    c=len(M[0])
    for i in range(r):
        for j in range(c):
            print(str(M[i][j]).ljust(5,' '), end = " ")
        print()


########################################################################################################################################################################################
def minor(M):
    a=[]
    N=[]
    for i in range(len(M)):
        for j in range(len(M[0])):
            a.append(M[i][j])
        N.append(a)
        a=[]
    import sys
    y=0
    z=0
    print("Enter the row and column number of element you want the minor of.")
    y=int(input("Row number: "))
    z=int(input("Column number: "))

    if y>len(M):
        print("Error: Row number exceeds the number of rows in matrix.")
        sys.exit()
    elif z>len(M[0]):
        print("Error: Column number exceeds the number of columns in matrix.")
        sys.exit()
    else:
        del N[y-1]
        for i1 in range(len(N)):
            a2=N[i1]
            del a2[z-1]

    return N


########################################################################################################################################################################################
def minor_auto(M,r,c):
    a=[]
    N=[]
    for i in range(len(M)):
        for j in range(len(M[0])):
            a.append(M[i][j])
        N.append(a)
        a=[]

    import sys
    if r+1>len(M):
        print("Error: Row number exceeds the number of rows in matrix.")
        sys.exit()
    elif c+1>len(M[0]):
        print("Error: Column number exceeds the number of columns in matrix.")
        sys.exit()
    else:
        del N[r]
        for i1 in range(len(N)):
            a2=N[i1]
            del a2[c]

    return N


########################################################################################################################################################################################
def mult(M1,M2):
    if len(M1[0])!=len(M2):
        print("Error, matrices are not multiplicable.")
    else:
        M3=[]
        for i1 in range(len(M1)):
            a4=[]
            for j2 in range(len(M2[0])):
                a3=[]
                for x in range(len(M2)):
                   z=(M1[i1][x]*M2[x][j2])
                   a3.append(z)
                a4.append(sum(a3))
            print(a4)
            M3.append(a4)
    return M3


########################################################################################################################################################################################
def add(M1,M2):
    M3=[]
    a=[]
    if len(M1)!=len(M2):
        print("Error, matrices do not have the same number of rows")
        #sys.exit()
    elif len(M1[0])!=len(M2[0]):
        print("Error, matrices do not have the same number of columns")
        #sys.exit()
    else:
        for i in range(len(M1)):
            for j in range(len(M1[0])):
                a.append(M1[i][j]+M2[i][j])
            M3.append(a)
            a=[]

    return M3
        

########################################################################################################################################################################################
def det_2(M):
    x=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return int(x)


########################################################################################################################################################################################
def det_3(M):
    x=0
    a=[]
    y=0
    N=[]
    for i in range(3):
        N=minor_auto(M,0,i)
        x=((-1)**i)*M[0][i]*det(N)
        a.append(x)
        N=[]
    y=sum(a)
    return int(y)
  

########################################################################################################################################################################################
def det_4(M):
    x=0
    a=[]
    y=0
    for i in range(4):
        N=minor_auto(M,0,i)
        x=((-1)**i)*M[0][i]*det(N)
        a.append(x)
        N=[]
    y=sum(a)
    return int(y)


    
########################################################################################################################################################################################
def det(M):
    if len(M)==2:
        return det_2(M)
    elif len(M)==3:
        return det_3(M)
    elif len(M)==4:
        return det_4(M)
    else:
        return "This program cannot be used to find a determinant of that order.", "Why do you need the determinant of a matrix that size anyway?"


########################################################################################################################################################################################        
def inv(M):
    M2=[]
    N=[]
    x=0
    y=0
    z=0
    a=[]
    for i in range(len(M)):
        for j in range(len(M)):
            N=minor_auto(M,j,i)
            x=det(N)
            y=(-1)**(i+j)
            z=int(det(M))
            a.append(x*y/z)
        M2.append(a)
        a=[]
    return M2


########################################################################################################################################################################################            
def subtract(M1,M2):
    M3=[]
    a=[]
    if len(M1)!=len(M2):
        print("Error, matrices do not have the same number of rows")
        sys.exit()
    elif len(M1[0])!=len(M2[0]):
        print("Error, matrices do not have the same number of columns")
        sys.exit()
    else:
        for i in range(len(M1)):
            for j in range(len(M1[0])):
                a.append(M1[i][j]-M2[i][j])
            M3.append(a)
            a=[]

    return M3
        

########################################################################################################################################################################################
#def rank(M):
#    N=[]
#    x=0
#    for i in range(len(M)):
#        for j in range(len(M[0])):
#            N=minor_auto(M,i,j)
#            x=det(N)
#            if x!=0:
#                return 
            
        
