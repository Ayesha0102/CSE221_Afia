import sys
sys.setrecursionlimit(2**25)

N=int(input())
graph=[]
for i in range(N+1):
    graph.append([])
for i in range(N-1):
    U,V=list(map(int,input().split()))
    graph[U].append(V)
    graph[V].append(U)

def dfs(vertics,parent,height):
    path=(height,vertics)
    for i in graph[vertics]:
        if i!=parent:
            new_path=dfs(i,vertics,height+1)
            if new_path[0]>path[0]:
                path=new_path
    return path

distance,u=dfs(1,-1,0)
diameter,v=dfs(u,-1,0)
print(diameter)
print(u,v)