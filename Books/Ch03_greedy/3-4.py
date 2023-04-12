# 예제 3-4: 1이 될 때까지
# 99p
n, k = map(int, input().split())
count = 0
while n != 1:
    if n % k != 0:
        count += n % k
        n = k * (n // k)
    else:
        count += 1
        n = n // k

print(count)
