N,M=map(int,input().split())
U=list(map(int,input().split()))
V=list(map(int,input().split()))
W=list(map(int,input().split()))
adj_list=[]
for i in range(N):
    row=[]
    adj_list.append(row)
for i in range(M):
    adj_list[U[i]-1].append((V[i]-1,W[i]))
for vertex in range(N):
    edges=" ".join(f"({V+1},{W})" for V, W in adj_list[vertex] )
    print(f"{vertex+1}:{edges}")