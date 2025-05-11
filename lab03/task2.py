def max_val(array1,i,j):
    #i,j=0,N-1   
    if j==i:
        return array1[i]
    
    mid=(i+j)//2
    left_max=max_val(array1,i,mid)
    right_max=max_val(array1,mid+1,j)
    
    highest_i=max(array1[i:mid+1])
    #highest_j=max(array1[mid+1:j+1])
    highest_j=-9999999
    for k in range(mid+1,j+1):
        highest_j=max(highest_j,highest_i+((array1[k])**2))
    return max(left_max,right_max,highest_j)
N=int(input())
A=list(map(int,input().split()))
maximum=max_val(A,0,N-1)
print(maximum)