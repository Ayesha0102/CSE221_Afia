def sorting(array1):
    length=len(array1)

    for i in range (length-1):
        flag=False
        for j in range(length-1):
            if array1[j]>array1[j+1]:
                array1[j],array1[j+1]=array1[j+1],array1[j]
                flag=True
        if flag==False:
            break
inp=int(input())
array1=list(map(int,input().split()))
sorting(array1)
print(" ".join(map(str,array1)))

