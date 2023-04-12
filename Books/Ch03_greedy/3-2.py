# 예제 3-2: 큰 수의 법칙
# 93p

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
max_1 = data[0]
max_2 = data[1]

print(max_1 * k * (m // k) + max_2 * (m % k))
