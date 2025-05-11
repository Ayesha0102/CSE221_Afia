import heapq
N,M,S,D=list(map(int,input().split()))
w=list(map(int,input().split()))
adj_list=[[]for i in range(N+1)]
for i in range(M):
    u,v=list(map(int,input().split()))
    adj_list[u].append(v)
def beautiful_path(N,S,D,w,adj_list):
    inf=float('inf')
    dist=[inf]*(N+1)
    dist[S]=w[S-1]
    Heap=[(w[S-1],S)]
    while Heap:
        edges,ver=heapq.heappop(Heap)
        if ver==D:
            return edges
        if edges>dist[ver]:
            continue
        for next in adj_list[ver]:
            new=edges+w[next-1]
            if new<dist[next]:
                dist[next]=new
                heapq.heappush(Heap,(new,next))
    return -1
solve=beautiful_path(N,S,D,w,adj_list)
print(solve)