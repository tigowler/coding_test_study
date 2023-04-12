# 올바른 괄호
# Programmers / Level 2
from collections import deque


def solution(s):
    answer = True
    q = deque()

    for i in range(len(s)):
        # 1) ")"가 들어왔을 때
        if s[i] == ")":
            # 1-1) ")"가 들어왔는데 q가 비어있을 때
            if len(q) == 0:
                return False

            # 1-2-1) ")"가 들어왔는데 바로 앞 글자가 ")"면 둘 다 q에 추가
            # 1-2-2) 바로 앞 글자가 "("이면 둘 다 담지 않기
            a = q.pop()
            if a == ")":
                q.append(a)
                q.append(s[i])

        # 2) "("가 들어왔을 때, ")"를 기다리도록 q에 담기
        else:
            q.append(s[i])

    if len(q) > 0:
        return False

    return True