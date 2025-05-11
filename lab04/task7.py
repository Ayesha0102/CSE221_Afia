import math
N,Q=list(map(int,input().split()))
#X,K=list(map(int,input().split()))

connected_nodes=[]
for i in range(N+1):
    connected_nodes.append([])

for i in range(1,N+1,1):
    for j in range(1,N+1,1):
        if i!=j and math.gcd(i,j)==1:
            connected_nodes[i].append(j)
    connected_nodes[i].sort()

size=len(connected_nodes)
for i in range(Q):
    X,K=list(map(int,input().split()))

    if size>=K:
        print(connected_nodes[X][K-1])
    else:
        print("-1")