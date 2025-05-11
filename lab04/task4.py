N,M=list(map(int,input().split()))
U=list(map(int,input().split()))
V=list(map(int,input().split()))

list_degrees=[0]*(N+1)
for i in range (M):
    end_point1=U[i]
    end_point2=V[i]
    list_degrees[end_point1]+=1
    list_degrees[end_point2]+=1

count=0
for i in range(N+1):
    if list_degrees[i]%2==0:
        count=count
    else:
        count+=1
if count==0:
    print("YES")
elif count==2:
    print("YES")
else:
    print("NO")
