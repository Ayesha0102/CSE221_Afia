import sys
sys.setrecursionlimit(2*100000+5)

def DFS(start,adj_list,color,travarsal):

    color[start]=1
    travarsal.append(start)
    for next in adj_list[start]:
        if color[next]==0:
            DFS(next,adj_list,color,travarsal) 


N,M=list(map(int,input().split()))
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))

    
color=[0]*(N+1)
travarsal=[]      
adj_list=[]
for i in range(N+1):
    adj_list.append([])

for i in range(M):
    start,next=list1[i],list2[i]
        
    adj_list[start].append(next)
    adj_list[next].append(start)

DFS(1,adj_list,color,travarsal)
print(" ".join(map(str,travarsal)))
