# 예제 4-4: 게임 개발
# 118p
N, M = map(int, input().split())
cur_x, cur_y, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dir_x = [-1, 0, 1, 0] # 북동남서
dir_y = [0, 1, 0, -1]
count = 1
visited = [[False for _ in range(N)] for _ in range(M)]
visited[cur_x][cur_y] = True
turn_time = 0

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

while True:
    turn_left() # 방향 전환
    next_x = cur_x + dir_x[d]
    next_y = cur_y + dir_y[d]
    if maps[next_x][next_y] == 0 and not visited[next_x][next_y]: # 갈 수 있는 위치라면,
        visited[next_x][next_y] = True # 방문 표시
        cur_x = next_x # 위치 이동
        cur_y = next_y
        count += 1 # 칸 수 추가
        turn_time = 0 # 회전 횟수 초기화
        continue

    else: # 바다 위치이거나 이미 방문한 곳일 때
        turn_time += 1 # 회전 횟수 증가

    if turn_time == 4: # 4방향을 다 돌았으나 갈 곳이 없는 경우
        next_x = cur_x - dir_x[d] 
        next_y = cur_y - dir_y[d]
        if maps[next_x][next_y] == 0: # 한 칸 후퇴할 수 있는 상황이라면,
            cur_x = next_x
            cur_y = next_y
            turn_time = 0 # 회전 횟수 초기화
        else: # 후퇴도 불가능한 경우, 더 이상 탐색할 수 없으니 종료
            break

print(count)

