def maxScore(s):
    n=len(s)
    zero_list=[0]*n
    one_list=[0]*n
    zero=0
    one=0
    for i in range(n):
        if s[i]=="0":
            zero+=1
            zero_list[i]=zero
        else:
            zero_list[i]=zero
    for j in range(n-1,-1,-1):
        if s[j]=="1":
            one+=1
            one_list[j]=one
        else:
            one_list[j]=one
    maxi=0
    for k in range(n-1):
        if maxi < zero_list[k]+one_list[k+1]:
            maxi = zero_list[k]+one_list[k+1]
    return maxi
