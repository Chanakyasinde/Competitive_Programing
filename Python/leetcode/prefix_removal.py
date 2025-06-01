def longest_prefix(s):
    n = len(s)
    for i in range(1, n + 1):
        prefix = s[:i]
        if s.find(prefix, i) != -1: 
            return i
    return 0

def process_string(s):
    while True:
        x = longest_prefix(s)
        if x == 0:
            break
        s = s[x:] 
    return s


t = int(input().strip())
results = []

for _ in range(t):
    s = input().strip()
    result = process_string(s)
    results.append(result)

for res in results:
    print(res)
