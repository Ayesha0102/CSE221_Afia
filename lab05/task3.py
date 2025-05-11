from collections import deque

N,M,S,D=list(map(int,input().split()))
U=list(map(int,input().split()))
V=list(map(int,input().split()))

adj_list=[]
for i in range(N+1):
    adj_list.append([])
for i in range(M):
    start,next=U[i],V[i]
    adj_list[start].append(next)
    adj_list[next].append(start)
for vertexs in adj_list:
    vertexs.sort()

pred=[-1]*(N+1)
edges=[-1]*(N+1)

Q=deque()
edges[S]=0
Q.append(S)
path=False
while Q:
    node=Q.popleft()
    if node==D:
        path=True
        break
    for ver in adj_list[node]:
        if edges[ver]==-1:
            edges[ver]=edges[node]+1
            pred[ver]=node
            Q.append(ver)
if not path:
    print("-1")
else:
    travarsal=[]
    nodes=D
    while nodes!=-1:
        travarsal.append(nodes)
        nodes=pred[nodes]
    print(edges[D])
    print(" ".join(map(str,reversed(travarsal))))
