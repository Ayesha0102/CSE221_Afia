from collections import deque
def BFS(N,adj_list):
    color=[0]*(N+1)
    Q=deque()
    
    start=1
    color[start]=1
    Q.append(start)
    travarsal=[]
    
    while Q:
        u=Q.popleft()
        travarsal.append(str(u))

        for v in adj_list[u]:
            if not color[v]:
                color[v]=1
                Q.append(v)

    print(" ".join(travarsal))

N,M=list(map(int,input().split()))
adj_list=[]
for i in range (N+1):
    adj_list.append([])


for i in range(M):
    u,v=list(map(int,input().split()))
    #for u,v in adj_list:
    adj_list[u].append(v)
    adj_list[v].append(u)
    #adj_list.app

BFS(N,adj_list)