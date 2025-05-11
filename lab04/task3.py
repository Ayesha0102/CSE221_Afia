N=int(input()) 
adj_mat=[]
for i in range(N):
    row=[]
    for j in range(N):
        row.append(0)
    adj_mat.append(row)
for i in range(N):
    k=list(map(int,input().split()))
    initial=k[0]
    vertex=k[1:]
    for j in vertex:
        adj_mat[i][j]=1
for i in range (N):
    for j in range(N):
        print(adj_mat[i][j],end=" ")
    print()