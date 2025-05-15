import sys
sys.setrecursionlimit (2**25)

N,K=(map(int,input().split()))
prev=[]
for i in range(N+1):
    prev.append(i)
circle=[1]*(N+1)

def friend(prev,x):
    if prev[x] !=x:
        prev[x]=friend(prev,prev[x])
    return prev[x]
def dsu(prev,circle,p1,p2):
    parent_p1=friend(prev,p1)
    parent_p2=friend(prev,p2)

    if parent_p1!=parent_p2:
        if circle[parent_p1]<circle[parent_p2]:
            parent_p1,parent_p2=parent_p2,parent_p1
        prev[parent_p2]=parent_p1
        circle[parent_p1]+=circle[parent_p2]
    return circle[parent_p1]

for i in range (K):
    f1,f2=(map(int,input().split()))
    size=dsu(prev,circle,f1,f2)
    print(size)