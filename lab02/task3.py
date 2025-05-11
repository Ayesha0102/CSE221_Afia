
def subarray(N,K,array1):
    pointer1=0
    sum1=0
    length=0
    for i in range(N):
        sum1+=array1[i]
        while sum1>K:
            sum1=sum1-array1[pointer1]
            pointer1=pointer1+1
        length=max(length,i-pointer1+1)
    return length
        
N,K=map(int,input().split())
array1=list(map(int,input().split()))
print(subarray(N,K,array1))