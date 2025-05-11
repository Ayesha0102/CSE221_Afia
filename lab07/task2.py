import heapq
N,M,S,T=list(map(int,input().split()))
'''u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))'''
adj_list=[[]for i in range(N+1)]
for i in range(M):
    u,v,w=list(map(int,input().split()))
    adj_list[u].append((v,w))
def dij(s):
    inf=float('inf')
    dist=[inf]*(N+1)
    dist[s]=0
    Heap=[(0,s)]
    while Heap:
        curr,ver=heapq.heappop(Heap)
        if curr>dist[ver]:
            continue
        for (next,edges) in adj_list[ver]:
            if dist[next]> dist[ver]+ edges :
                dist[next]=dist[ver]+edges
                heapq.heappush(Heap,(dist[next],next))
    return dist
A=dij(S)
B=dij(T)

min_t=float('inf')
meet_at=-1
for i in range(1,N+1):
    if A[i]!=min_t and B[i]!=min_t:
        max_t=max(A[i],B[i])
        if max_t<min_t or (max_t==min_t and i<meet_at):
             min_t=max_t
             meet_at=i
if meet_at== -1:
    print("-1")
else:
    print(f'{min_t} {meet_at}')

