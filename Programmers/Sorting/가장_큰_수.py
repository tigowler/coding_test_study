# 참고: https://school.programmers.co.kr/questions/45680

def solution(numbers):
    strs = []
    for num in numbers:
        strs.append(str(num))

    strs.sort(key=lambda x: (x*4)[:4], reverse=True)
    answer = ''.join(strs)

    if answer[0] == '0':
        answer = '0'

    return answer


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))