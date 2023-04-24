# 참고: https://jeongmin.tistory.com/5
from collections import deque


def solution(n, wires):
    graph = [[] for _ in range(n + 1)] # n이 4일 때, 0~4까지 리스트를 만들고 1~4까지만 사용
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start):
        visited = [0] * (n + 1)
        q = deque([start])
        visited[start] = 1
        cnt = 1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1

        return cnt

    answer = n
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        answer = min(abs(bfs(a) - bfs(b)), answer)

        graph[a].append(b)
        graph[b].append(a)

    return answer
