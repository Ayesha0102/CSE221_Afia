import heapq

N,M,S,D=(map(int,input().split()))
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))
adj_list=[]
for i in range(N+1):
    adj_list.append([])
for i in range(M):
   adj_list[u[i]].append((v[i],w[i]))

dist=[float("inf")]*(N+1)
dist[S]=0
prev=[-1]*(N+1)
Heap=[(0,S)]

while Heap: 
    current,vertex=heapq.heappop(Heap)
    if current>dist[vertex]:
        continue
    for (ver,edges) in adj_list[vertex]:
        if dist[ver]>dist[vertex]+edges:
            dist[ver]=dist[vertex]+edges
            prev[ver]=vertex
            heapq.heappush(Heap,(dist[ver],ver))
if dist[D]==float("inf"):
    print("-1")
else:    
    print(dist[D])
    direction=[]
    vertex=D
    while vertex!=-1:
        direction.append(vertex)
        vertex=prev[vertex]
    direction.reverse()
    print(" ".join(map(str,direction)))         

