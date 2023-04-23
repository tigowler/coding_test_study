answer = -1


def dfs(cur_hp, dungeons, visited, count):
    global answer
    # 현재 피로도로 갈 수 있는 던전이 없는 경우
    for d in dungeons:
        if cur_hp < d[0]:
            pass
        else:
            break
    else:
        answer = count if answer < count else answer
        return

    # 모든 던전을 다 방문한 경우
    if count == len(dungeons):
        answer = count if answer < count else answer
        return

    for i in range(len(dungeons)):
        if dungeons[i][0] <= cur_hp and not visited[i]:
            visited[i] = True
            dfs(cur_hp - dungeons[i][1], dungeons, visited, count + 1)
            visited[i] = False


def solution(k, dungeons):
    global answer
    visited = [False for _ in range(len(dungeons))]
    dfs(k, dungeons, visited, 0)
    return answer


k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))