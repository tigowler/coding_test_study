# 다리를 지나는 트럭
# Programmers / Level 2
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_queue = deque(truck_weights) # 전체 트럭
    bridge_queue = deque([]) # 다리를 건너는 트럭

    while True:
        weight_sum = 0 # 다리를 건너는 중인 트럭의 전체 무게

        # 전체 트럭도, 다리를 건너는 중인 트럭도 없다면 종료
        if not truck_queue:
            if not bridge_queue:
                break

        answer += 1 # 시간 경과

        # 맨 앞 트럭이 다리를 모두 건넜다면 삭제
        if bridge_queue:
            if bridge_queue[0][1] >= bridge_length:
                bridge_queue.popleft()

        # 1씩 앞으로 이동
        if bridge_queue:
            for i in range(len(bridge_queue)):
                bridge_queue[i][1] += 1

        # 다리를 건너는 중인 트럭의 총 무게 계산
        if bridge_queue:
            for i in range(len(bridge_queue)):
                weight_sum += bridge_queue[i][0]

        # 대기 트럭이 있다면,
        if truck_queue:
            # 다리에 남는 자리가 있고, 다음 트럭을 추가해도 무게가 초과하지 않는다면,
            if len(bridge_queue)+1 <= bridge_length and (weight_sum+truck_queue[0])<=weight:
                truck = truck_queue.popleft()
                bridge_queue.append([truck, 1])

    return answer

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

print(solution(bridge_length, weight, truck_weights))