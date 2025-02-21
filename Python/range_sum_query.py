arr=list(map(int,input().split()))
n=len(arr)
prefix=[0]*n
for i in range(n):
    if i==0:
        prefix[i]=arr[i]
    else:
        prefix[i]=prefix[i-1]+arr[i]
q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    if l==0:
        print(prefix[r])
    else:
        print(prefix[r]-prefix[l-1])
