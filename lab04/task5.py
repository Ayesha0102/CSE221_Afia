N,M=list(map(int,input().split()))
U=list(map(int,input().split()))
V=list(map(int,input().split()))

list_indeg=[0]*(N+1)
list_outdeg=[0]*(N+1)

for i in range(M):
    point1=U[i]
    list_outdeg[point1]+=1

    point2=V[i]
    list_indeg[point2]+=1

output=[]
for i in range(1,N+1):
    diff=list_indeg[i]-list_outdeg[i]
    output.append(diff)

print(" ".join(map(str,output)))
