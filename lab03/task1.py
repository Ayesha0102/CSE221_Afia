def merge (a,b):
    i,j=0,0
    inversion=0
    list1=[]
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            list1.append(a[i])
            i+=1
        else:
            list1.append(b[j])
            inversion+=len(a)-i
            j+=1
    list1.extend(a[i:])
    list1.extend(b[j:])
    return list1, inversion 

def merge_sort(array1):
    if len(array1)<2:
        return array1,0

    mid=len(array1)//2
    a,left_inv=merge_sort(array1[:mid])
    b,right_inv=merge_sort(array1[mid:])
    list1, inverse_merge=merge(a,b)
    return list1, left_inv+right_inv+inverse_merge

N=int(input())
A=list(map(int,input().split()))
sorted,inversion_count=merge_sort(A)
print(inversion_count)
print(*sorted)