INF = 99999

def floyd(G,v):
    d = G
    for k in range (v):
        for i in range (v):
            for j in range(v):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    display(d,v)

def display(d,v):
    print ("Distance Matrix")
    for i in range(v):
        for j in range(v):
                print(d[i][j],"\t",end=" ")
        print()


v = int (input("Enter number of Vertices:\n"))
G = []

for i in range (v):
    a = []
    for j in range (v):
        r = int (input("Enter distance:"))
        a.append(r)
    G.append(a)
floyd(G,v)