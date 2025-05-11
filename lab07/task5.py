import heapq
N,M=(map(int,input().split()))
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))
   
adj_list=[]
for i in range(N+1):
    adj_list.append([])
for i in range(M):
    U=u[i]
    V=v[i]
    W=w[i]
    adj_list[U].append((V,W))
    adj_list[V].append((U,W))
inf=float("inf")
dist=[]
for i in range(N+1):
    dist.append([inf,inf])
visit=[]
for i in range(N+1):
    visit.append([False,False])
Heap=[]
dist[1][0]=0
dist[1][1]=0
heapq.heappush(Heap,(0,1,0))

while Heap:
    weight,curr_node,latest=heapq.heappop(Heap)
    if visit[curr_node][latest]:
        continue
    visit[curr_node][latest]=True
    for V,W in adj_list[U]:
        new=W%2
        if new==latest:
            continue

        if new!=latest:
            new_weight=weight+W
            if dist[V][new]>new_weight:
                    dist[V][new]=new_weight
                    heapq.heappush(Heap,(dist[V][new],V,new))
min_dist=min(dist[N])
if min_dist != inf:
    print(min_dist)
'''else:
    print ("-1")'''

