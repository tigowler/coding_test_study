# 만들어지는 모든 수에 대해 소수인지 검사하면, 시간 초과로 통과하지 못하는 테스트 케이스가 발생함
# 중복되는 수를 반복적으로 검사하기 때문.
# 따라서, 만들어지는 모든 수를 중복 제거한 다음 한꺼번에 소수 검사 진행.
import math

answer = set()  # numbers로 만들 수 있는 수를 중복 제거 후 저장


def dfs(cur, depth, numbers, used):
    global answer
    answer.add(cur)

    if depth == len(numbers):
        return

    for i in range(len(numbers)):
        if not used[i]:
            new_num = cur * 10 + int(numbers[i])
            used[i] = True
            dfs(new_num, depth + 1, numbers, used)
            used[i] = False
            dfs(cur, depth + 1, numbers, used)


def is_prime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    global answer
    result = 0  # 소수의 개수

    used = [False for _ in range(len(numbers))]
    dfs(0, 0, numbers, used)

    for n in list(answer):
        if is_prime(n):
            result += 1

    return result