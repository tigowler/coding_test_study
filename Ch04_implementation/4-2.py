# 예제 4-2: 시각
# 113p
def solution():
    N = int(input())
    count = 0
    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                res = change_string(i, j, k)
                count = count + 1 if res.count('3') > 0 else count

    print(count)


def change_string(h, m, s):
    hour = str(h) if len(str(h)) >= 2 else "0" + str(h)
    minute = str(m) if len(str(m)) >= 2 else "0" + str(m)
    sec = str(s) if len(str(s)) >= 2 else "0" + str(s)

    return hour + "시 " + minute + "분 " + sec + "초"


solution()
