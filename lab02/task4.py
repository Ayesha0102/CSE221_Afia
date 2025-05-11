def binary_string(string1):
    left=0
    right=len(string1)-1
    idx=-1
    while left<=right:
        mid=(left+right)//2
        if string1[mid]=='1':
            idx=mid+1
            right=mid-1
        else:
            left=mid+1
    return (idx)

test_case=int(input().strip())
for i in range(test_case):
    string1=input().strip()
    print(binary_string(string1))