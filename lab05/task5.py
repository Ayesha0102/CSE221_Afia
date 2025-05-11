import sys
sys.setrecursionlimit(2*100000 +5)

N,M=list(map(int,input().split()))
adj_list=[]
for i in range(N+1):
    adj_list.append([])
for i in range(M):
    U,V=list(map(int,input().split()))
    adj_list[U].append(V)
def DFS(U):
    track[U]=1
    for V in adj_list[U]:
        if track[V]==0:
            if DFS(V):
                return True
        elif track[V]==1:
            return True
    track[U]=2
    return False
track=[0]*(N+1)
for i in range(N+1):
    if track[i]==0:
        if DFS(i):
            print("YES")
            break
else:
    print("NO")
