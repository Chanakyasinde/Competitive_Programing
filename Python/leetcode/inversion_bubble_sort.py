def count_inversions(list_of_numbers):
    n=len(list_of_numbers)
    count=0
    for j in range(n-1):
        for i in range(1,n):
            if list_of_numbers[i-1]>list_of_numbers[i]:
                list_of_numbers[i-1],list_of_numbers[i]=list_of_numbers[i],list_of_numbers[i-1]
                count+=1
    return count
