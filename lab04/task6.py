N=int(input())
x,y=list(map(int,input().split()))

possible_cell=[]

for i in range(x-1,x+2,1):
    for j in range(y-1,y+2,1):
        if (i,j)!=(x,y):
            if i<1 or j<1 or i>N or j>N:
                continue

            else:
                possible_cell.append((i,j))
total_cell=len(possible_cell)
print(total_cell)

for row,col in possible_cell:
    print(row,col)