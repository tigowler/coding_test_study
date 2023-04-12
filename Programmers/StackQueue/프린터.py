# 프린터
# Programmers / Level 2
from collections import deque

def solution(priorities, location):
    answer = 0
    files = deque() # 우선순위 저장
    locations = deque() # 초기 위치 저장

    for i in range(len(priorities)):
        files.append(priorities[i])
        locations.append(i)

    while (files):
        cur_file = files.popleft()
        cur_loc = locations.popleft()
        priorities[cur_loc] = 0

        # 1) 가장 우선순위가 높은 문서인지 확인
        if cur_file >= max(priorities):
            # 1-1) 가장 우선순위 높은 문서인 경우, 찾고 있는 문서인지 확인
            if cur_loc == location:
                # 1-1-1) 찾고 있는 문서인 경우, answer 반환
                return answer+1
            # 1-1-2) 찾는 게 아닐 경우 pass
            else:
                answer += 1

        else:
            # 1-2) 가장 높지 않은 경우, 맨 뒤로 보내기
            files.append(cur_file)
            locations.append(cur_loc)
            priorities[cur_loc] = cur_file

    return answer