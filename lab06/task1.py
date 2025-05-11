from collections import deque
def order(N,M,prereq):
    indegree=[0]*(N+1)
    adj_dict={}
    for A,B in prereq:
        if A not in adj_dict:
            adj_dict[A]=[]
        adj_dict[A].append(B)
        indegree[B]+=1
    Q=deque()
    for i in range(1,N+1):
        if indegree[i]==0:
            Q.append(i)
    result=[]

    while Q:
        U=Q.popleft()
        result.append(U)
        if U in adj_dict:
            for V in adj_dict[U]:
                indegree[V]-=1
                if indegree[V]==0:
                    Q.append(V)
    if len(result)==N:
        return result
    else:
        print ("-1")

N,M=list(map(int,input().split()))
prereq=[tuple(map(int,input().split())) for _ in range(M)]
solve=order(N,M,prereq)
print(" ".join(map(str,solve)))
     
