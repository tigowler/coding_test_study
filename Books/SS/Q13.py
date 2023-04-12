# 치킨 배달
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house_list = []
chicken_list = []
chosen_chicken_list = []
answer = 1e9

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken_list.append((i, j))
        if graph[i][j] == 1:
            house_list.append((i, j))


def dfs(depth, idx):
    global answer
    if depth == m:
        sum = 0
        for house in house_list:
            val = 1e9
            for chosen_chicken in chosen_chicken_list:
                tmp = abs(house[0]-chosen_chicken[0]) + abs(house[1]-chosen_chicken[1])
                val = min(tmp, val)
            sum += val
        answer = min(answer, sum)
        return

    for i in range(idx, len(chicken_list)): # combination
        if chicken_list[i] in chosen_chicken_list:
            continue

        chosen_chicken_list.append(chicken_list[i])
        dfs(depth+1, i+1)
        chosen_chicken_list.pop()

dfs(0, 0)
print(answer)