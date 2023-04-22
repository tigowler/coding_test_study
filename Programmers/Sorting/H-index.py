# 참고: https://school.programmers.co.kr/questions/47194

def solution(citations):
    answer = 0
    citations.sort() # [0, 1, 3, 5, 6]
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i: # h번 이상 인용된 논문이 h편 이상
            answer += 1

    return answer