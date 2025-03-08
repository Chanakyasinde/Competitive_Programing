def bubbleSort(seq):
    n=len(seq)
    for i in range(n-1):
        for j in range(1,n):
            if seq[j-1]>seq[j]:
                seq[j-1],seq[j]=seq[j],seq[j-1]
    return seq
