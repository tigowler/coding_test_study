# 예제 3-3: 숫자 카드 게임
# 96p
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
max_num = 1
for cards_row in a:
    if max_num < min(cards_row):
        max_num = min(cards_row)

print(max_num)