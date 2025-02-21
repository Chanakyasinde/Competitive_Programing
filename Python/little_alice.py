n=int(input())
arr=list(map(int,input().split()))
prefix=[0]*n
if arr[0]%5==0:
    prefix[0]=1
else:
    prefix[0]=0
for i in range(1,n):
    if arr[i]%5==0:
        prefix[i]=prefix[i-1]+1
    else:
        prefix[i]=prefix[i-1]
q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    if l==0:
        print(prefix[r])
    else:
        print(prefix[r]-prefix[l-1])  
