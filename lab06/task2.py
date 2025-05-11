from collections import deque

N,M=list(map(int,input().split()))
graph=[]
for i in range(N+1):
    graph.append([])
for i in range(M):
    U,V=list(map(int,input().split()))
    graph[U].append(V)
    graph[V].append(U)

visit=[False]*(N+1)
Hu_or_ro=[-1]*(N+1)
def bfs(s):
    Q=deque([s])
    visit[s]=True
    Hu_or_ro[s]=0
    
    count=[s]
    
    while Q:
        U=Q.popleft()
      
        for V in graph[U]:
            if not visit[V]:
                visit[V]=True
                Hu_or_ro[V]=1-Hu_or_ro[U]
                count.append(V)
                Q.append(V)
            elif Hu_or_ro[V]==Hu_or_ro[U]:
                return 0
    zero=0
    one=0
    for i in count:
        if Hu_or_ro[i]==0:
            zero+=1
        else:
            one+=1
    return max(zero,one)
    
result=0
for i in range(1,N+1):
    if not visit[i]:
        if not graph[i]:
            result+=1
            visit[i]=True
        else:
            result+=bfs(i)
print(result)
    