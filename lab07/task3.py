import heapq
N,M=list(map(int,input().split()))
adj_list=[[] for i in range(N+1)]
for i in range(M):
    u,v,w=list(map(int,input().split()))
    adj_list[u].append((v,w))
    adj_list[v].append((u,w))
def danger(N,M,adj_list):
    Heap=[]
    inf=float('inf')
    min_danger=[inf]*(N+1)
    min_danger[1]=0
    heapq.heappush(Heap,(0,1))
    while Heap:
        curr,city=heapq.heappop(Heap)
        if curr>min_danger[city]:
            continue
        for v,edges in adj_list[city]:
            new=max(curr,edges)
            if new<min_danger[v]:
                min_danger[v]=new
                heapq.heappush(Heap,(new,v))
    path=[]
    for i in range(1,N+1):
        if min_danger[i]==inf:
            path.append(-1)
        else:
            path.append(min_danger[i])
    return path
path=danger(N,M,adj_list)
print(" ".join(map(str,path)))