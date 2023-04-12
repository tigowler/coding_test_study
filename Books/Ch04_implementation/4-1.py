# 예제 4-1: 상하좌우
# 110p
def is_inside(x, y, n):
    if x < 1 or y < 1 or x > n or y > n:
        return False
    return True


def solution():
    n = int(input())
    plans = list(input().split())
    dir_x = [-1, 1, 0, 0]  # 상하좌우
    dir_y = [0, 0, -1, 1]
    cur_x = 1
    cur_y = 1
    dir_nums = {"U": 0, "D": 1, "L": 2, "R": 3}

    for plan in plans:
        next_x = cur_x + dir_x[dir_nums[plan]]
        next_y = cur_y + dir_y[dir_nums[plan]]

        if is_inside(next_x, next_y, n):
            cur_y = next_y
            cur_x = next_x

    print((cur_x, cur_y))


solution()
