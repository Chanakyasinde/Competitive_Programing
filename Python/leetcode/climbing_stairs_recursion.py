def recursion(arr,n):
    if arr[n]!=-1:
        return arr[n]
    if n==0 or n==1:
        return 1
    else:
        arr[n] = recursion(arr,n-1)+recursion(arr,n-2)
        return arr[n]

def climbStairs(n):
    arr=[-1]*(n+1)
    return recursion(arr,n)
