n,k = map(int, input().split())
a = list(map(int, input().split()))

max_sum = current_sum = sum(a[:k])

for i in range(k, n):
    current_sum += a[i] - a[i - k]  
    max_sum = max(max_sum, current_sum)


print(max_sum)
