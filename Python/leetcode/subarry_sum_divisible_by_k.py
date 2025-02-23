n, k = map(int, input().split())
nums = list(map(int, input().split()))

prefix_sum = 0
count = 0
remainder_count = {}  
remainder_count[0] = 1  

for num in nums:
    prefix_sum += num
    remainder = prefix_sum % k
    
    if remainder < 0:
        remainder += k
    
    if remainder in remainder_count:
        count += remainder_count[remainder]
    
    if remainder in remainder_count:
        remainder_count[remainder] += 1
    else:
        remainder_count[remainder] = 1

print(count)
