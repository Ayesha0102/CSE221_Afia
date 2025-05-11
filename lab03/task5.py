def bst(array1):
    if not array1:
        return []

    mid=len(array1)//2
    return [array1[mid]]+ bst(array1[:mid])+bst(array1[mid+1:])

N=int(input())
A=list(map(int,input().split()))
print(*bst(A))