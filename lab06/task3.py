from collections import deque
possible_moves=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
def knight_move(N,X1,Y1,X2,Y2): 
    visit=[[-1]*(N+1) for i in range(N+1)]
    if (X1,Y1) == (X2,Y2):
        return 0
 
    visit[X1][Y1]=0
    Q=deque()
    Q.append((X1,Y1))

    
    while Q:
        r,c=Q.popleft()
    
        for dr,dc in possible_moves:
            new_r=r+dr
            new_c=c+dc

            if 1<=new_r<=N and 1<=new_c<=N and  visit[new_r][new_c]==-1:
                    visit[new_r][new_c]=visit[r][c]+1
                    Q.append((new_r,new_c))
    return visit[X2][Y2]
N=int(input())
X1,Y1,X2,Y2=map(int,input().split())
print(knight_move(N,X1,Y1,X2,Y2))