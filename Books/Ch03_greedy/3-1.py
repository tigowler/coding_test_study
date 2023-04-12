# 예제 3-1: 거스름돈
# 87p

def solution(N):
    coins = [500, 100, 50, 10]
    count = 0
    cur_cash = N
    for coin in coins:
        count += cur_cash//coin
        cur_cash = cur_cash % coin

    return count