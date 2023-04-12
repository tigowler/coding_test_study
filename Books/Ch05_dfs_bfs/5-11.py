# 예제 5-11: 미로 탈출
# 152p
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 벗어나는 경우
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            # 해당 위치에 괴물이 있는 경우
            if graph[nx][ny] == 0:
                continue
            # 해당 위치를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))

