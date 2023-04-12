# 타겟 넘버
# Programmers / Level 2
answer = 0

def solution(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer

def DFS(pos, numbers, target, res):
    global answer
    if pos == len(numbers):
        if res == target:
            answer += 1
        return

    DFS(pos + 1, numbers, target, res + numbers[pos])
    DFS(pos + 1, numbers, target, res - numbers[pos])