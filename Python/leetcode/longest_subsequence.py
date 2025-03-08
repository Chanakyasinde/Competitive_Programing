# # def subsequence(nums,j,n,arr,total):
# #     if j==n:
# #         if (len(arr)!=0):
# #             sm = sum(arr)
# #             ln = len(arr)
# #             temp = [sm,ln]
# #             total.append(temp)
# #         return 0
# #     subsequence(nums,j+1,n,arr,total)
# #     arr.append(nums[j])
# #     subsequence(nums,j+1,n,arr,total)
# #     arr.pop()

# def answerQueries(nums, queries):
#     n=len(nums)
#     m=len(queries)
#     arr=[]
#     total=[]
#     prev_sum = 0
#     prev_len = 0
#     for i in range(len(nums)):
#         temp = 
#         total.append()

#     # print(total)
#     max_ln = []
#     for q in queries:
#         q_len = 0
#         for i in range(len(total)):
#             # print(total[i])
#             if (total[i][0]<=q and total[i][1]>q_len):
#                 q_len=total[i][1]
#         max_ln.append(q_len)
#     # print(max_ln)
#     return max_ln

def answerQueries(nums, queries):
    # Sort the array to take smallest elements first
    nums.sort()
    
    # Create prefix sum array to quickly calculate subsequence sums
    prefix_sums = []
    curr_sum = 0
    for num in nums:
        curr_sum += num
        prefix_sums.append(curr_sum)
    print(prefix_sums)
    # Process each query
    answer = []
    for query in queries:
        # Binary search to find largest index where prefix sum <= query
        left, right = 0, len(nums) - 1
        max_length = 0
        
        while left <= right:
            mid = (left + right) // 2
            if prefix_sums[mid] <= query:
                max_length = mid + 1  # +1 because length is index + 1
                left = mid + 1
            else:
                right = mid - 1
                
        answer.append(max_length)
    
    return answer
