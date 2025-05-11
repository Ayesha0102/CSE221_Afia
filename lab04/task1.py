N,M=map(int,input().split())
adj_mat=[]
for i in range(N):
    row=[]
    for i in range(N):
        row.append(0)
    adj_mat.append(row)
for i in range(M):
    u,v,w=map(int,input().split())
    adj_mat[u-1][v-1]=w
for row in adj_mat:
    print(" ".join(map(str,row)))
