# 예제 5-10: 음료수 얼려 먹기
# 149p
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
count = 0


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m: # 범위 밖으로 벗어나면 즉시 False 반환
        return False

    if graph[x][y] == 0: # 칸막이가 존재하지 않는 부분인 경우,
        graph[x][y] = 1 # 다시 또 방문 하지 않도록 바로 1로 표시
        # 상하좌우 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)