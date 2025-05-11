def MOD(a,b):
    a=a%107
    answer=1
    while b>0:
        if b%2==1:
            answer=(answer*a)%107
        a=(a*a)%107
        b=b//2
    return answer
a,b=map(int,input().split())
print(MOD(a,b))