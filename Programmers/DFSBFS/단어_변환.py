# 단어 변환
# programmers / Level 3
from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque()
    q.append((begin,0))

    while q:
        visited = [0]*len(words)
        b,idx = q.popleft()
        if b == target:
            break

        for k in range(len(words)):
            for j in range(len(words[k])):
                if b[j] == words[k][j]:
                    visited[k] +=1

        for k in range(len(visited)):
            if visited[k] == (len(target)-1):
                q.append((words[k],idx+1))
                words[k] = str(idx)


    return idx