# 퇴사
n = int(input())
t = [] # 각 상담을 완료하는 데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    time = i + t[i]
    if time <= n : # 상담이 기간 안에 끝나는 경우
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else: # 상담이 기간을 벗어나는 경우
        dp[i] = max_value

print(max_value)