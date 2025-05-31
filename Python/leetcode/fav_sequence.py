q=int(input())
for _ in range(q):
    n=int(input())
    lst=list(map(int,input().split()))
    new=[0]*n
    x,y=0,n-1
    for i in range(n):
        if i%2==0:
            new[i]=lst[x]
            x+=1
        else:
            new[i]=lst[y]
            y-=1
    print(*new)
