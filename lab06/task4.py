import sys
sys.setrecursionlimit(10**6)

N,R=list(map(int,input().split()))
graph=[]
for i in range(N+1):
    graph.append([])
for i in range(N-1):
    U,V=list(map(int,input().split()))
    graph[U].append(V)
    graph[V].append(U)
subtree=[1]*(N+1)

def dfs(vertics,parent):
    
    for i in graph[vertics]:
        if i!=parent:
            dfs(i,vertics)
            subtree[vertics]+=subtree[i]
dfs(R,-1)
Q=int(input())
for i in range(Q):
    query_nodes=int(input())
    print(subtree[query_nodes])