def merged(n1,arr1,n2,arr2):
    point1=0
    point2=0
    result=[]
    while point1<n1 and point2<n2:
        if arr1[point1]<=arr2[point2]:
            result.append(arr1[point1])
            point1+=1
        else:
            result.append(arr2[point2])
            point2+=1
    if point1<n1:
        result.extend(arr1[point1:])
    if point2<n2:
        result.extend(arr2[point2:])
    print(" ".join(map(str,result)))
n1=int(input().strip())
arr1=list(map(int,input().split()))
n2=int(input().strip())

arr2=list(map(int,input().split()))
merged(n1,arr1,n2,arr2)