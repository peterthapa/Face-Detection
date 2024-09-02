def bicoeff(n,r):
    c=[[0 for j in range (r+1)] for i in range (n+1)]
    for i in range(n+1):
        for j in range (r+1):
            if (j<=i):
                if (j==0 or j==i):
                    c[i][j] = 1
                else:
                    c[i][j] = c[i-1][j-1]+c[i-1][j]
    print (n,"C",r, " = ", c[n][r])

n = int(input("n = "))
r = int(input("r = "))
bicoeff(n,r)



