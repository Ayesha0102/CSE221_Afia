def sum_trouble(inp,sum,array1):
    i=0
    j=inp-1
    while i<j:
        temp=array1[i]+array1[j]
        if temp==sum:
            print(i+1,j+1)
            return
        elif temp<sum:
            i=i+1
        elif temp>sum:
            j=j-1
        
    print("-1")
inp,sum=map(int,input().split())
array1=list(map(int,input().split()))
sum_trouble(inp,sum,array1)