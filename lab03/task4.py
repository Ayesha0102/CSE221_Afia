def fast_MOD(a,n,m):
    temp=1
    while n:
        if n%2:
            temp=(temp*a)%m
        a=(a*a)%m
        n//=2
    return temp
def calc(a,n,m):
    if a==1:
        print(n%m)
    else:
        result=(fast_MOD(a,n+1,m*(a-1))-a)//(a-1)%m
        print(result)
test_case=int(input())
for i in range(test_case):
    a,n,m=map(int,input().split())
    calc(a,n,m)