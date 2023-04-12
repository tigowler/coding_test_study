# 같은 숫자는 싫어
# Programmers / Level 1
def solution(arr):
    answer = [arr[0]]
    pre = arr[0]
    for i in range(1, len(arr)):
        if arr[i]==pre:
            continue
        else:
            answer.append(arr[i])
        pre = arr[i]
    return answer