len,n =map(int,input().split())
array1=list(map(str,input().split()))

for i in range(n//2):
    array1[i],array1[n-i-1]=array1[n-i-1],array1[i]
print(" ".join(array1[:n])) 