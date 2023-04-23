# 참고: https://school.programmers.co.kr/questions/47460

def solution(brown, yellow):
    size = brown + yellow
    for i in range(size + 1, 1, -1):
        if size%i == 0:
            j = size//i
            if (i-2) * (j-2) == yellow:
                return [i, j]

brown = 24
yellow = 24
print(solution(brown, yellow))
