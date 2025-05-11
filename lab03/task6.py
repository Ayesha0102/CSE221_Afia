def postorder(inorder,preorder):
    if len(inorder)==0: 
        return []
    root=preorder[0]
    idx=inorder.index(root)
    
    left=postorder(inorder[:idx],preorder[1:idx+1])
    right=postorder(inorder[idx+1:],preorder[idx+1:])

    return left+right+[root]
N=int(input())
inorder=list(map(int,input().split()))
preorder=list(map(int,input().split()))
a=postorder(inorder,preorder)
print(" ".join(map(str,a)))
