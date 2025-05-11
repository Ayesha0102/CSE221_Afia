def search_in_left(array1,first):
    l=0
    r=len(array1)
    while l<r:
        mid=(l+r)//2
        if array1[mid]<first:
            l=mid+1
        else:
            r=mid
    return l
def search_in_right(array1,second):
    l=0
    r=len(array1)
    while l<r:
        mid=(l+r)//2
        if array1[mid]<=second:
            l=mid+1
        else:
            r=mid
    return l

n,quary=map(int,input().split())
array1=list(map(int,input().split()))
for i in range(quary):
    first,second=map(int,input().split())
    print(search_in_right(array1,second)-search_in_left(array1,first))