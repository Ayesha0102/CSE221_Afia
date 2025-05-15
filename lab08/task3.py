import sys
sys.setrecursionlimit(2**25)
N,M=list(map(int,input().split()))
roads=[]
for i in range(M):
    U,V,W=(map(int,input().split()))
    roads.append((W,U,V))
roads.sort()

prev=[]
for i in range(N+1):
    prev.append(i)
depth=[0]*(N+1)

def solve (prev,x):
    if prev[x]!=x:
        prev[x]=solve(prev,prev[x])
    return prev[x]
def dsu(prev,depth,city1,city2):
    parent_c1=solve(prev,city1)
    parent_c2=solve(prev,city2)
    if parent_c1==parent_c2:
        return False
    if depth[parent_c1]<depth[parent_c2]:
        prev[parent_c1]=parent_c2
    prev[parent_c2]=parent_c1
    if depth[parent_c1]==parent_c2:
        depth[parent_c1]+=1
    return True

